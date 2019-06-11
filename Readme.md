1. Run main.py - trains a model and extracts raw rule json into data/extracted_rules.jsonj
2. Run simplify_rules.py - loads data/extracted_rules.json and eliminates redundant rules. `Eg: greater than 2 and greater than 3 becomes greater than 3` 
3. Run refactor_rules.py - simplifies rules by introducing variable-like clauses
4. Run human_readable_rules.py - to extract human readable rules
