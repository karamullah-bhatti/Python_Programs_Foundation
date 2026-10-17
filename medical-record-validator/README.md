# Medical Record Validator

A Python script that validates patient records for correct data types, required keys, and specific formats using regular expressions.

## Key Concepts Used
- **Type Checking**: Uses `isinstance()` for robust data validation.
- **Regular Expressions**: Uses `re.fullmatch()` to enforce ID patterns (e.g., `p1001`, `v2301`).
- **Dictionary Unpacking**: Leverages `**` to pass record data directly into validation functions.
- **Error Reporting**: Iterates through invalid records using `enumerate()` and formatted f-strings.

## How to Run
```bash
python medical_records.py
