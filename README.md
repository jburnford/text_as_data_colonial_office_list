# Colonial Office List Extraction Workshop

Extract structured personnel data from 19th-century Colonial Office Lists using regex and LLMs.

## Quick Start (No Installation Required)

### Option 1: Google Colab Notebook
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jburnford/textasdatacolonialofficelist/blob/main/Colonial_Office_List_Extraction.ipynb)

The notebook includes:
- Sample source text (Sierra Leone 1896)
- Regex extraction code
- LLM prompt template for AI Studio
- Evaluation against gold standard

### Option 2: Google AI Studio (LLM Extraction)
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Follow instructions in [STUDENT_GUIDE.md](STUDENT_GUIDE.md)
3. Copy the prompt, paste your source text, run

## What You'll Learn

1. **Regex-based extraction** - Pattern matching for structured historical text
2. **LLM code generation** - Have an AI write reviewable Python code containing extracted data
3. **Evaluation** - Compare extraction results against a gold standard

## Repository Contents

| File | Description |
|------|-------------|
| `Colonial_Office_List_Extraction.ipynb` | Colab notebook with complete workflow |
| `STUDENT_GUIDE.md` | Step-by-step guide for AI Studio |
| `extraction_regex.py` | Standalone regex extractor |
| `extraction_codegen.py` | Automated LLM code generation (requires API key) |
| `test_data/sierra_leone_1896_test.txt` | Sample source text |
| `test_data/gold_standard.json` | Manually verified extraction (42 officials) |
| `generated/` | Example LLM-generated extraction code |

## The Key Insight

Instead of asking an LLM to extract data directly (non-deterministic, hard to verify), we ask it to **generate Python code** containing the data. This gives us:

- **Reviewable output** - Read the code, check for errors
- **Deterministic results** - Run the code, get the same JSON every time
- **Version control** - Commit the generated code to git

## Sample Source Text

```
Colonial Secretary's Department.

Colonial Secretary, Lt.-Col. J. O. Gore, 710l. to 800l., and quarters.
Assistant Colonial Secretary, E. Faulkner, 300l. to 350l.
Chief Clerk, J. E. Dawson, 200l.
2nd ditto, E. W. Cole, 100l. to 120l.
```

## Sample Extraction Output

```json
{
  "name": "J. O. Gore",
  "canonical_name": "Gore, J. O.",
  "position": "Colonial Secretary",
  "department": "Colonial Secretary's Department - Sierra Leone",
  "salary_min": 710,
  "salary_max": 800,
  "military_rank": "Lt.-Col."
}
```

## Evaluation Results

| Method | Recall | Precision | Cost |
|--------|--------|-----------|------|
| Regex | 100% | 95% | Free |
| Gemini 2.0 Flash | 100% | 98% | Free (AI Studio) |

See [EXTRACTION_COMPARISON.md](EXTRACTION_COMPARISON.md) for detailed analysis.

## License

Educational use. Source data from Colonial Office Lists (public domain).
