# Colonial Office List Extraction in R

This guide shows how to extract structured data from Colonial Office Lists using R. If you're comfortable with R but not Python, this approach will feel familiar.

## Setup

```r
# Install packages (if needed)
install.packages(c("stringr", "jsonlite", "tidyverse"))

# Load libraries
library(stringr)
library(jsonlite)
library(tidyverse)
```

## Load the Source Text

```r
# Read the source file
source_text <- readLines("test_data/sierra_leone_1896_test.txt", warn = FALSE)
source_text <- paste(source_text, collapse = "\n")

# Or paste directly:
source_text <- "
Colonial Secretary's Department.

Colonial Secretary, Lt.-Col. J. O. Gore, 710l. to 800l., and quarters.
Assistant Colonial Secretary, E. Faulkner, 300l. to 350l.
Chief Clerk, J. E. Dawson, 200l.
2nd ditto, E. W. Cole, 100l. to 120l.
"
```

## Define Regex Patterns

```r
# Salary patterns
salary_range_pattern <- "(\\d+)l\\.\\s*to\\s*(\\d+)l\\."
salary_single_pattern <- "(\\d+)l\\."

# Honors (appear after names)
honors_pattern <- "\\b(K\\.?C\\.?M\\.?G|C\\.?M\\.?G|G\\.?C\\.?M\\.?G|K\\.?C\\.?B|C\\.?B|D\\.?S\\.?O)\\.?"

# Qualifications (medical/academic)
quals_pattern <- "\\b(M\\.?D|M\\.?B|M\\.?R\\.?C\\.?S|F\\.?R\\.?C\\.?S|L\\.?R\\.?C\\.?P|B\\.?A|M\\.?A|LL\\.?D)\\.?"

# Military ranks
military_pattern <- "^(Colonel|Lt\\.-Col\\.|Major|Captain|Capt\\.)\\s+"

# Department headers
dept_pattern <- "^[A-Z][A-Za-z\\s']+Department\\.?$"
```

## Parse Salaries

```r
parse_salary <- function(text) {
  # Try range first: "300l. to 400l."
  range_match <- str_match(text, salary_range_pattern)
  if (!is.na(range_match[1])) {
    return(list(
      salary_min = as.integer(range_match[2]),
      salary_max = as.integer(range_match[3])
    ))
  }

  # Try single: "200l."
  single_match <- str_match(text, salary_single_pattern)
  if (!is.na(single_match[1])) {
    salary <- as.integer(single_match[2])
    return(list(salary_min = salary, salary_max = salary))
  }

  return(list(salary_min = NA, salary_max = NA))
}

# Test it
parse_salary("710l. to 800l.")
# $salary_min: 710, $salary_max: 800
```

## Extract Honors and Qualifications

```r
extract_honors <- function(text) {
  matches <- str_match_all(text, honors_pattern)[[1]]
  if (nrow(matches) > 0) {
    # Normalize format (add periods)
    honors <- matches[, 2]
    honors <- str_replace_all(honors, "([A-Z])(?=[A-Z])", "\\1.")
    if (!str_detect(honors, "\\.$")) honors <- paste0(honors, ".")
    return(honors)
  }
  return(character(0))
}

extract_qualifications <- function(text) {
  matches <- str_match_all(text, quals_pattern)[[1]]
  if (nrow(matches) > 0) {
    quals <- matches[, 2]
    quals <- str_replace_all(quals, "([A-Z])(?=[A-Z])", "\\1.")
    if (!str_detect(quals, "\\.$")) quals <- paste0(quals, ".")
    return(quals)
  }
  return(character(0))
}

# Test
extract_honors("Colonel F. Cardew, C.M.G., 2000l.")
# "C.M.G."

extract_qualifications("W. T. Prout, M.B., 50l.")
# "M.B."
```

## Extract Military Rank

```r
extract_military_rank <- function(text) {
  match <- str_match(text, military_pattern)
  if (!is.na(match[1])) {
    return(match[2])
  }
  return(NA)
}

# Test
extract_military_rank("Lt.-Col. J. O. Gore, 710l.")
# "Lt.-Col."
```

## Handle "Ditto" References

The Colonial Office Lists use "ditto" to avoid repeating position types:
- "Chief Clerk" followed by "2nd ditto" means "2nd Clerk"
- "Colonial Surgeon" followed by "Assistant ditto" means "Assistant Colonial Surgeon"

```r
expand_ditto <- function(position, previous_position) {
  if (!str_detect(position, "ditto")) {
    return(position)
  }

  # Extract the base position type (e.g., "Clerk" from "Chief Clerk")
  base_type <- str_extract(previous_position, "\\w+$")

  # Replace "ditto" with the base type
  expanded <- str_replace(position, "ditto", base_type)
  return(expanded)
}

# Test
expand_ditto("2nd ditto", "Chief Clerk")
# "2nd Clerk"

expand_ditto("Assistant ditto", "Colonial Surgeon")
# "Assistant Surgeon"
```

## Full Extraction Function

```r
extract_officials <- function(text, colony = "Sierra Leone", year = 1896) {
  lines <- str_split(text, "\n")[[1]]
  lines <- str_trim(lines)
  lines <- lines[lines != ""]

  officials <- list()
  current_dept <- NA
  previous_position <- NA

  for (line in lines) {
    # Check for department header
    if (str_detect(line, dept_pattern)) {
      current_dept <- str_remove(line, "\\.$")
      current_dept <- paste0(current_dept, " - ", colony)
      next
    }

    # Skip lines without salary (headers, etc.)
    if (!str_detect(line, "\\d+l\\.")) {
      next
    }

    # Parse the line
    salary <- parse_salary(line)
    honors <- extract_honors(line)
    quals <- extract_qualifications(line)
    military <- extract_military_rank(line)

    # Extract position (everything before first comma or name)
    position <- str_extract(line, "^[^,]+")
    position <- str_remove(position, military_pattern)
    position <- str_trim(position)

    # Handle ditto
    if (str_detect(position, "ditto") && !is.na(previous_position)) {
      position <- expand_ditto(position, previous_position)
    }
    previous_position <- position

    # Extract name (between position and salary/honors)
    # This is the trickiest part - names come after position
    name_section <- str_remove(line, paste0("^", str_escape(position), ",?\\s*"))
    name_section <- str_remove(name_section, military_pattern)

    # Remove salary and everything after
    name_section <- str_remove(name_section, "\\d+l\\..*$")

    # Remove honors and qualifications from name
    name_section <- str_remove_all(name_section, honors_pattern)
    name_section <- str_remove_all(name_section, quals_pattern)
    name_section <- str_remove_all(name_section, ",\\s*$")
    name_section <- str_trim(name_section)

    # Parse name into parts
    name_parts <- str_match(name_section, "^([A-Z]\\.\\s*)+([A-Z][a-z]+)$")

    official <- list(
      name = name_section,
      position = position,
      department = current_dept,
      salary_min = salary$salary_min,
      salary_max = salary$salary_max,
      honors = if (length(honors) > 0) honors else list(),
      qualifications = if (length(quals) > 0) quals else list(),
      military_rank = military,
      colony = colony,
      year = year
    )

    officials <- append(officials, list(official))
  }

  return(officials)
}
```

## Run the Extraction

```r
# Extract officials
officials <- extract_officials(source_text)

# Convert to data frame for analysis
df <- bind_rows(lapply(officials, function(x) {
  x$honors <- paste(x$honors, collapse = "; ")
  x$qualifications <- paste(x$qualifications, collapse = "; ")
  as.data.frame(x, stringsAsFactors = FALSE)
}))

# View results
print(df)
```

## Export to JSON

```r
# Export to JSON (matches Python output format)
result <- list(
  colony = "Sierra Leone",
  year = 1896,
  total_officials = length(officials),
  officials = officials
)

json_output <- toJSON(result, pretty = TRUE, auto_unbox = TRUE)
write(json_output, "sierra_leone_1896_r.json")

cat(json_output)
```

## Compare with Gold Standard

```r
# Load gold standard
gold <- fromJSON("test_data/gold_standard.json")

# Compare counts
cat("Extracted:", length(officials), "\n")
cat("Gold standard:", length(gold$officials), "\n")

# Check specific fields
gold_names <- sapply(gold$officials, function(x) x$name)
extracted_names <- sapply(officials, function(x) x$name)

# Find matches
matched <- sum(extracted_names %in% gold_names)
cat("Names matched:", matched, "/", length(gold_names), "\n")
```

## Tips for R Users

### String Functions Comparison

| Python | R (stringr) |
|--------|-------------|
| `re.search(pattern, text)` | `str_detect(text, pattern)` |
| `re.findall(pattern, text)` | `str_match_all(text, pattern)` |
| `re.sub(pattern, repl, text)` | `str_replace(text, pattern, repl)` |
| `text.split('\n')` | `str_split(text, '\n')` |
| `text.strip()` | `str_trim(text)` |

### Regex Differences

R uses double backslashes for escape sequences:
- Python: `\d+`
- R: `\\d+`

### Working with Lists vs Data Frames

The extraction returns a list of lists (like Python's list of dicts). Convert to a data frame for easier analysis:

```r
# List of officials -> data frame
df <- bind_rows(officials)

# Now you can use tidyverse operations
df %>%
  group_by(department) %>%
  summarise(
    count = n(),
    avg_salary = mean(salary_min, na.rm = TRUE)
  )
```

## Exercise

1. Load `test_data/sierra_leone_1896_test.txt`
2. Extract all officials using the functions above
3. Export to JSON
4. Compare your extraction count to the gold standard (42 officials)
5. Which officials are missing? Why?

## Resources

- [stringr cheat sheet](https://stringr.tidyverse.org/)
- [R regex tutorial](https://r4ds.had.co.nz/strings.html)
- [jsonlite package](https://cran.r-project.org/web/packages/jsonlite/)
