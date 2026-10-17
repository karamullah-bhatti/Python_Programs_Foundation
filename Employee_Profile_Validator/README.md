# Employee Profile Cleaner & Validator

A Python utility script designed to process, clean, and extract information from employee profile data (names, emails, addresses, and codes) using built-in string methods.

## Key Concepts Used
- **Searching & Slicing**: Using `.find()` and slicing (`[:at_position]`) to extract usernames from emails.
- **Cleaning & Formatting**: Using `.strip()`, `.lower()`, `.upper()`, and `.title()` to normalize messy user inputs.
- **Substitution & Splitting**: Using `.replace()` to clean phone numbers and `.split()` / `.join()` to handle address formatting.
- **Validation Checks**: Using `in`, `.startswith()`, `.endswith()`, and `.count()` to verify patterns and data integrity.

## How to Run
```bash
python employee_profile.py
