#!/usr/bin/env python3
"""
Transform britishempire_kg_export.cypher to fix issues identified in Gemini review.

Changes:
  1. Node labels: Colony → HistoricalTerritory + specific labels
  2. Relationships: EVOLVED_INTO/SUCCESSOR_TO with relationship_type → typed rels
  3. Data types: lat/lon strings → floats, add point(), normalize dates
  4. Princely States: established_year → dynasty_founded
  5. Constraint updated for new label
"""

import re
import sys
from datetime import datetime

# ── Label mapping ──
# Maps administrative_status values to (specific_label, remove_colony)
ADMIN_STATUS_TO_LABEL = {
    'Crown Colony': ('CrownColony', False),
    'Crown colony': ('CrownColony', False),
    'Royal Colony': ('CrownColony', False),
    'Protectorate': ('Protectorate', False),
    'Colony/Protectorate': ('Protectorate', False),
    'Occupation/Protectorate': ('Protectorate', False),
    'Dominion': ('Dominion', False),
    'Mandate': ('Mandate', False),
    'Mandate/Trust Territory': ('Mandate', False),
    'Trust Territory': ('Mandate', False),
    'Independence': ('IndependentNation', True),
    'Unilateral Independence': ('IndependentNation', True),
    'Guano Island': ('MinorTerritory', False),
    'Whaling Station': ('MinorTerritory', False),
    'Remote Island': ('MinorTerritory', False),
    'Company Territory': ('CompanyTerritory', False),
    'Trading Post': ('CompanyTerritory', False),
    'Company Settlement': ('CompanyTerritory', False),
    'Boer Republic': ('BoerRepublic', True),
    'Federation': ('Federation', False),
    'Federal Colony': ('Federation', False),
    'Province': ('Province', False),
    'Presidency': ('Province', False),
    'United Province': ('Province', False),
    'Division of a Presidency': ('Province', False),
    'Dependency': ('Dependency', False),
    'British Overseas Territory': ('OverseasTerritory', False),
    'Condominium': ('Condominium', False),
    'Anglo-French Condominium': ('Condominium', False),
    'Military Administration': ('MilitaryAdministration', False),
}

# ── Relationship type mapping ──
# Maps relationship_type property values to (new_rel_type, detail_value)
EVOLVED_INTO_MAPPING = {
    'BECAME_INDEPENDENT': 'BECAME_INDEPENDENT',
    'INDEPENDENCE_GRANTED': 'BECAME_INDEPENDENT',
    'INDEPENDENCE_RESTORED': 'BECAME_INDEPENDENT',
    'MERGED_INTO': 'MERGED_INTO',
    'MERGED_WITH': 'MERGED_INTO',
    'BECAME_PART_OF': 'MERGED_INTO',
    'AMALGAMATED_INTO': 'MERGED_INTO',
    'INCORPORATED_INTO': 'INCORPORATED_INTO',
    'REORGANIZED_AS': 'REORGANIZED_AS',
    'RENAMED_TO': 'REORGANIZED_AS',
    'EXPANDED_TO': 'REORGANIZED_AS',
    'EXPANDED_WITH_PROTECTORATE': 'REORGANIZED_AS',
    'CONSOLIDATED_AS_PROVINCE': 'REORGANIZED_AS',
    'INTERNAL_SETTLEMENT': 'REORGANIZED_AS',
    'BECAME_CROWN_COLONY': 'BECAME_CROWN_COLONY',
    'BECAME_COLONY': 'BECAME_COLONY',
    'FORMALIZED_AS_COLONY': 'BECAME_COLONY',
    'BECAME_PROTECTORATE': 'BECAME_PROTECTORATE',
    'BECAME_MANDATE': 'BECAME_MANDATE',
    'BECAME_SEPARATE_COLONY': 'BECAME_SEPARATE_COLONY',
    'BECAME_SELF_GOVERNING': 'BECAME_SELF_GOVERNING',
    'FEDERATED_INTO': 'FEDERATED_INTO',
    'CONFEDERATED_INTO': 'FEDERATED_INTO',
    'JOINED_FEDERATION': 'FEDERATED_INTO',
    'JOINED_CONFEDERATION': 'FEDERATED_INTO',
    'JOINED': 'FEDERATED_INTO',
    'FEDERATION_SUCCESSION': 'FEDERATED_INTO',
    'PARTITIONED_INTO': 'PARTITIONED_INTO',
    'PARTITIONED_TO': 'PARTITIONED_INTO',
    'SEPARATED_INTO': 'PARTITIONED_INTO',
    'CARVED_OUT': 'PARTITIONED_INTO',
    'SEPARATED_FROM': 'PARTITIONED_INTO',
    'SEPARATED_FROM_INDIA': 'PARTITIONED_INTO',
    'TRANSFERRED_TO_CROWN': 'TRANSFERRED_SOVEREIGNTY',
    'TRANSFERRED_TO_AUSTRALIA': 'TRANSFERRED_SOVEREIGNTY',
    'CONQUERED_BY': 'TRANSFERRED_SOVEREIGNTY',
    'CONQUERED_AND_RENAMED': 'TRANSFERRED_SOVEREIGNTY',
    'RETURNED_TO': 'TRANSFERRED_SOVEREIGNTY',
    'RESTORED_TO_CROWN': 'TRANSFERRED_SOVEREIGNTY',
    'ANNEXED_BY': 'TRANSFERRED_SOVEREIGNTY',
    'REUNITED_INTO': 'REUNITED_INTO',
    'DIRECT_SUCCESSION': 'EVOLVED_INTO',
}


# ── QID name resolutions (manually verified by domain expert) ──
QID_NAMES = {
    'Q101242542': 'Kadana State',
    'Q104152112': 'Surat State',
    'Q104152114': 'Yasin State',
    'Q11904734': 'Alaniawas',
    'Q11905355': 'Ammayanayakan',
    'Q11905439': 'Anakapalle',
    'Q11905698': 'Antarbella',
    'Q11908900': 'Bedam',
    'Q131080302': 'Sudasana State',
    'Q134436280': 'Bilkha',
    'Q1632695': 'Sanjeli State',
    'Q21044436': 'Edappalli',
    'Q21075438': 'Gopalpet',
    'Q21075439': 'Kaddatanad',
    'Q48838868': 'Tharad State',
    'Q48838869': 'Wao State',
    'Q48838872': 'Santalpur State',
    'Q48838989': 'Sarila State',
}


def try_float(val):
    """Try to parse a value as float, return string representation."""
    if val is None:
        return None
    val = val.strip().strip("'\"")
    try:
        return str(float(val))
    except ValueError:
        return f"'{val}'"


def normalize_date(val):
    """Normalize date values to ISO 8601 string."""
    if val is None:
        return None
    val = val.strip().strip("'\"")

    # Already an ISO date string
    if re.match(r'^\d{4}-\d{2}-\d{2}', val):
        return f"'{val}'"

    # Unix epoch (integer)
    try:
        epoch = int(val)
        # Milliseconds if > 1e12
        if epoch > 1e12:
            epoch = epoch / 1000
        dt = datetime.utcfromtimestamp(epoch)
        return f"'{dt.strftime('%Y-%m-%dT%H:%M:%S')}'"
    except (ValueError, OSError):
        pass

    return f"'{val}'"


def parse_node_block(lines):
    """Parse a MERGE node block and return transformed lines."""
    block = '\n'.join(lines)

    # Detect if this is a Princely State
    is_princely = "colony_type: 'Princely State'" in block

    # Determine labels
    admin_match = re.search(r"administrative_status: '([^']+)'", block)
    admin_status = admin_match.group(1) if admin_match else None

    colony_type_match = re.search(r"colony_type: '([^']+)'", block)
    colony_type = colony_type_match.group(1) if colony_type_match else None

    # Build label string
    labels = ['HistoricalTerritory']
    remove_colony = False

    if is_princely:
        labels.append('PrincelyState')
        remove_colony = True
    elif admin_status and admin_status in ADMIN_STATUS_TO_LABEL:
        specific, remove = ADMIN_STATUS_TO_LABEL[admin_status]
        labels.append(specific)
        remove_colony = remove
    elif colony_type and colony_type in ADMIN_STATUS_TO_LABEL:
        specific, remove = ADMIN_STATUS_TO_LABEL[colony_type]
        labels.append(specific)
        remove_colony = remove

    if not remove_colony:
        labels.append('Colony')

    label_str = ':'.join(labels)

    # Replace Colony label in MERGE line
    result = []
    for line in lines:
        # Fix the MERGE label — handle existing multi-labels like Colony:Dominion
        line = re.sub(r'MERGE \(c:[\w:]+ ', f'MERGE (c:{label_str} ', line)

        # Cast latitude to float
        lat_match = re.search(r"latitude: '([^']+)'", line)
        if lat_match:
            try:
                float_val = float(lat_match.group(1))
                line = line.replace(f"latitude: '{lat_match.group(1)}'", f"latitude: {float_val}")
            except ValueError:
                pass

        # Cast longitude to float
        lon_match = re.search(r"longitude: '([^']+)'", line)
        if lon_match:
            try:
                float_val = float(lon_match.group(1))
                line = line.replace(f"longitude: '{lon_match.group(1)}'", f"longitude: {float_val}")
            except ValueError:
                pass

        # Normalize created_date epoch integers
        cd_match = re.search(r'created_date: (\d{10,13})', line)
        if cd_match:
            epoch = int(cd_match.group(1))
            if epoch > 1e12:
                epoch = epoch / 1000
            try:
                dt = datetime.utcfromtimestamp(epoch)
                line = line.replace(
                    f"created_date: {cd_match.group(1)}",
                    f"created_date: '{dt.strftime('%Y-%m-%dT%H:%M:%S')}'"
                )
            except (OSError, ValueError):
                pass

        # Normalize spatial_updated epoch integers
        su_match = re.search(r'spatial_updated: (\d{10,13})', line)
        if su_match:
            epoch = int(su_match.group(1))
            if epoch > 1e12:
                epoch = epoch / 1000
            try:
                dt = datetime.utcfromtimestamp(epoch)
                line = line.replace(
                    f"spatial_updated: {su_match.group(1)}",
                    f"spatial_updated: '{dt.strftime('%Y-%m-%dT%H:%M:%S')}'"
                )
            except (OSError, ValueError):
                pass

        # Normalize created_date in BORDERS_WITH / NEAR_COAST_OF relationships too
        # (handled separately in relationship processing)

        # Princely State: rename established_year → dynasty_founded
        if is_princely:
            line = line.replace('established_year:', 'dynasty_founded:')

        # Resolve QID-only names
        qid_name_match = re.search(r"name: '(Q\d+)'", line)
        if qid_name_match:
            qid = qid_name_match.group(1)
            if qid in QID_NAMES:
                line = line.replace(f"name: '{qid}'", f"name: '{QID_NAMES[qid]}'")

        result.append(line)

    return result


def transform_relationship(line):
    """Transform a relationship line."""
    # Skip non-relationship lines
    if not line.strip().startswith('MATCH'):
        return line

    # Handle EVOLVED_INTO with relationship_type property
    evolved_match = re.search(
        r'\[:EVOLVED_INTO \{([^}]+)\}\]',
        line
    )
    if evolved_match:
        props_str = evolved_match.group(1)

        # Extract relationship_type
        rt_match = re.search(r"relationship_type: '([^']+)'", props_str)
        if rt_match:
            orig_type = rt_match.group(1)
            new_rel_type = EVOLVED_INTO_MAPPING.get(orig_type, 'EVOLVED_INTO')

            # Remove relationship_type from props, add detail
            new_props = re.sub(r",?\s*relationship_type: '[^']+'", '', props_str)
            new_props = new_props.strip().strip(',').strip()
            if new_props:
                new_props += f", detail: '{orig_type}'"
            else:
                new_props = f"detail: '{orig_type}'"

            line = line.replace(
                f'[:EVOLVED_INTO {{{evolved_match.group(1)}}}]',
                f'[:{new_rel_type} {{{new_props}}}]'
            )

    # Handle SUCCESSOR_TO with relationship_type → SUCCEEDED
    successor_match = re.search(
        r'\[:SUCCESSOR_TO \{([^}]+)\}\]',
        line
    )
    if successor_match:
        props_str = successor_match.group(1)

        rt_match = re.search(r"relationship_type: '([^']+)'", props_str)
        if rt_match:
            orig_type = rt_match.group(1)

            # Remove relationship_type from props, add detail
            new_props = re.sub(r",?\s*relationship_type: '[^']+'", '', props_str)
            new_props = new_props.strip().strip(',').strip()
            if new_props:
                new_props += f", detail: '{orig_type}'"
            else:
                new_props = f"detail: '{orig_type}'"

            line = line.replace(
                f'[:SUCCESSOR_TO {{{successor_match.group(1)}}}]',
                f'[:SUCCEEDED {{{new_props}}}]'
            )
        else:
            # Bare SUCCESSOR_TO without relationship_type
            line = line.replace('[:SUCCESSOR_TO]', '[:SUCCEEDED]')
            line = re.sub(
                r'\[:SUCCESSOR_TO \{([^}]+)\}\]',
                r'[:SUCCEEDED {\1}]',
                line
            )

    # Clean BORDERS_WITH: remove relationship_type property
    borders_match = re.search(r'\[:BORDERS_WITH \{([^}]+)\}\]', line)
    if borders_match:
        props = borders_match.group(1)
        props = re.sub(r",?\s*relationship_type: '[^']+'", '', props)
        props = props.strip().strip(',').strip()

        # Also normalize created_date epoch in relationship props
        cd_match = re.search(r'created_date: (\d{10,13})', props)
        if cd_match:
            epoch = int(cd_match.group(1))
            if epoch > 1e12:
                epoch = epoch / 1000
            try:
                dt = datetime.utcfromtimestamp(epoch)
                props = props.replace(
                    f"created_date: {cd_match.group(1)}",
                    f"created_date: '{dt.strftime('%Y-%m-%dT%H:%M:%S')}'"
                )
            except (OSError, ValueError):
                pass

        if props:
            line = re.sub(
                r'\[:BORDERS_WITH \{[^}]+\}\]',
                f'[:BORDERS_WITH {{{props}}}]',
                line
            )

    # Clean NEAR_COAST_OF: remove relationship_type property
    coast_match = re.search(r'\[:NEAR_COAST_OF \{([^}]+)\}\]', line)
    if coast_match:
        props = coast_match.group(1)
        props = re.sub(r",?\s*relationship_type: '[^']+'", '', props)
        props = props.strip().strip(',').strip()

        cd_match = re.search(r'created_date: (\d{10,13})', props)
        if cd_match:
            epoch = int(cd_match.group(1))
            if epoch > 1e12:
                epoch = epoch / 1000
            try:
                dt = datetime.utcfromtimestamp(epoch)
                props = props.replace(
                    f"created_date: {cd_match.group(1)}",
                    f"created_date: '{dt.strftime('%Y-%m-%dT%H:%M:%S')}'"
                )
            except (OSError, ValueError):
                pass

        if props:
            line = re.sub(
                r'\[:NEAR_COAST_OF \{[^}]+\}\]',
                f'[:NEAR_COAST_OF {{{props}}}]',
                line
            )

    # Update Colony label references in MATCH clauses
    line = re.sub(r'\(a:Colony \{', '(a:HistoricalTerritory {', line)
    line = re.sub(r'\(b:Colony \{', '(b:HistoricalTerritory {', line)

    return line


def main():
    input_file = 'britishempire_kg_export.cypher'
    output_file = 'britishempire_kg_export_v2.cypher'

    with open(input_file, 'r') as f:
        lines = f.readlines()

    output = []
    i = 0

    # Write new header
    output.append('// British Empire Knowledge Graph — Territory nodes and relationships\n')
    output.append(f'// Exported from Neo4j, cleaned on {datetime.now().strftime("%Y-%m-%d")}\n')
    output.append('//\n')
    output.append('// Node labels: HistoricalTerritory (base), Colony, CrownColony, Protectorate,\n')
    output.append('//   Dominion, Mandate, PrincelyState, IndependentNation, Federation,\n')
    output.append('//   Province, CompanyTerritory, MinorTerritory, BoerRepublic, etc.\n')
    output.append('//\n')
    output.append('// To import: run this file in Neo4j Browser or cypher-shell\n')
    output.append('\n')

    # Updated constraint
    output.append('// ── Constraints ──\n')
    output.append('CREATE CONSTRAINT territory_id_unique IF NOT EXISTS FOR (n:HistoricalTerritory) REQUIRE n.colony_id IS UNIQUE;\n')
    output.append('\n')
    output.append('// ── Territory Nodes ──\n')
    output.append('\n')

    # Skip original header and constraint
    while i < len(lines):
        line = lines[i].rstrip('\n')

        # Skip original header/comments/constraint
        if i < 10 and (line.startswith('//') or line.startswith('CREATE CONSTRAINT') or line.strip() == ''):
            i += 1
            continue

        # Node block: starts with MERGE (c:Colony or MERGE (c:Colony:Dominion etc.
        if re.match(r'MERGE \(c:Colony', line):
            block = [line]
            i += 1
            while i < len(lines) and not (lines[i].strip() == '' or lines[i].startswith('MERGE') or lines[i].startswith('MATCH') or lines[i].startswith('//')):
                block.append(lines[i].rstrip('\n'))
                i += 1

            transformed = parse_node_block(block)
            output.extend(l + '\n' for l in transformed)
            continue

        # Section comment for relationships
        if '── Relationships ──' in line:
            output.append('\n// ── Relationships ──\n')
            output.append('// Relationship types: EVOLVED_INTO, BECAME_INDEPENDENT, BECAME_CROWN_COLONY,\n')
            output.append('//   BECAME_COLONY, BECAME_PROTECTORATE, BECAME_MANDATE, BECAME_SEPARATE_COLONY,\n')
            output.append('//   BECAME_SELF_GOVERNING, MERGED_INTO, INCORPORATED_INTO, REORGANIZED_AS,\n')
            output.append('//   FEDERATED_INTO, PARTITIONED_INTO, TRANSFERRED_SOVEREIGNTY, REUNITED_INTO,\n')
            output.append('//   SUCCEEDED, PART_OF, WAS_MEMBER_OF, ADMINISTERED_UNDER,\n')
            output.append('//   BORDERS_WITH, NEAR_COAST_OF, TRANSFERRED_TERRITORY\n')
            output.append('\n')
            i += 1
            continue

        # Relationship lines
        if line.startswith('MATCH'):
            output.append(transform_relationship(line) + '\n')
            i += 1
            continue

        # Pass through everything else
        output.append(line + '\n')
        i += 1

    with open(output_file, 'w') as f:
        f.writelines(output)

    print(f"Wrote {output_file}")
    print(f"Lines: {len(lines)} → {len(output)}")

    # Print label summary
    label_counts = {}
    for line in output:
        m = re.search(r'MERGE \(c:([\w:]+)', line)
        if m:
            labels = m.group(1)
            label_counts[labels] = label_counts.get(labels, 0) + 1

    print("\nLabel distribution:")
    for labels, count in sorted(label_counts.items(), key=lambda x: -x[1]):
        print(f"  {labels}: {count}")

    # Print relationship type summary
    rel_counts = {}
    for line in output:
        m = re.search(r'\[:([\w]+)', line)
        if m and line.startswith('MATCH'):
            rel = m.group(1)
            rel_counts[rel] = rel_counts.get(rel, 0) + 1

    print("\nRelationship type distribution:")
    for rel, count in sorted(rel_counts.items(), key=lambda x: -x[1]):
        print(f"  {rel}: {count}")


if __name__ == '__main__':
    main()
