1. Run main.py - trains a model and extracts raw rule json into data/extracted_rules.jsonj
2. Run simplify_rules.py - loads data/extracted_rules.json and eliminates redundant rules. `Eg: greater than 2 and greater than 3 becomes greater than 3` 
4. Run refactor_rules.py - simplifies rules by introducing variable-like clauses
3. Run extract_fuzzy_rules.py - extracts feature ranges
