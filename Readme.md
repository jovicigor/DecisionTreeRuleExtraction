Rule extraction from Decision Tree Regressors
- 
This project is a research on how to extract rules from the existing data. 
The dataset used to train the model and extract rules is [Boston Housing Dataset](https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html). The goal is to extract the rules based on which the taxes are formed.

Rule extraction works as follows:
- Decision Tree Regressor is trained on data provided in data/apartments_sale.csv
- Decision tree is traversed and rules are extracted into data/extracted_rules.json file
- Since some rules are redundant they are simplified by simplify_rules.py script (Eg: greater than 2 and greater than 3 becomes greater than 3). 
- Simplified rules are then refactored - for all the pairs of conditions that exist in more than 5% of generated rules refactoring is performed: 
Each pair becomes a subrule that is then used as a 'variable' in the rules where the pair is found.  


## How to run

`NOTE: Make sure you have python 3.7 installed with all the requirements listed in requirements.txt`
1. Run main.py - trains a model and extracts raw rule json into data/extracted_rules.jsonj
2. Run simplify_rules.py - loads data/extracted_rules.json and eliminates redundant rules. `Eg: greater than 2 and greater than 3 becomes greater than 3` 
3. Run refactor_rules.py - simplifies rules by introducing variable-like clauses
4. Run human_readable_rules.py - extracts human readable rules and writes them to data/human_readable_rules.csv

After rules and subrules are extracted subrules can be renamed by experts in order to better match the domain.

## Boston Housing Example

There are 14 attributes in each case of the dataset. They are:

- CRIM - per capita crime rate by town
- ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
- INDUS - proportion of non-retail business acres per town.
- CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
- NOX - nitric oxides concentration (parts per 10 million)
- RM - average number of rooms per dwelling
- AGE - proportion of owner-occupied units built prior to 1940
- DIS - weighted distances to five Boston employment centres
- RAD - index of accessibility to radial highways
- TAX - full-value property-tax rate per $10,000
- PTRATIO - pupil-teacher ratio by town
- B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- LSTAT - % lower status of the population
- MEDV - Median value of owner-occupied homes in $1000's

|     |  Boston Housing Dataset tax rules                                                                                                                                                                                                                                                   | 
|----|-------------------------------------------------------------------------------------------| 
| 0  | SUBRULE_0: IF AND indus <= 26.695 AND nox <= 0.583 THEN SUBRULE_0                         | 
| 1  | SUBRULE_1: IF AND rad <= 16.0 AND nox > 0.583 THEN SUBRULE_1                              | 
| 2  | SUBRULE_2: IF AND rad IS IN RANGE (3.5, 16.0] AND dis <= 2.8589 THEN SUBRULE_2          | 
| 3  | SUBRULE_3: IF AND ptratio > 13.85 AND indus <= 20.735 THEN SUBRULE_3                      | 
| 4  | SUBRULE_4: IF AND ptratio > 13.85 AND indus IS IN RANGE (20.735, 26.695] THEN SUBRULE_4 | 
| 5  | SUBRULE_5: IF AND dis <= 6.2433 AND rad <= 3.5 THEN SUBRULE_5                             | 
| 6  | SUBRULE_6: IF AND dis > 6.2433 AND rad <= 3.5 THEN SUBRULE_6                              | 
| 7  | SUBRULE_7: IF AND rad <= 16.0 AND indus > 26.695 THEN SUBRULE_7                           | 
| 8  | SUBRULE_8: IF AND dis > 2.8589 AND rad IS IN RANGE (3.5, 16.0] THEN SUBRULE_8           | 
| 9  | SUBRULE_9: IF AND indus <= 26.695 AND ptratio <= 13.85 THEN SUBRULE_9                     | 
| 10 | IF SUBRULE_5 AND SUBRULE_0 THEN tax=233.8448275862069                                     | 
| 11 | IF SUBRULE_6 AND SUBRULE_0 THEN tax=328.0416666666667                                     | 
| 12 | IF SUBRULE_2 AND SUBRULE_0 THEN tax=376.8888888888889                                     | 
| 13 | IF SUBRULE_8 AND SUBRULE_0 THEN tax=299.8781725888325                                     | 
| 14 | IF SUBRULE_9 AND SUBRULE_1 THEN tax=264.0                                                 | 
| 15 | IF SUBRULE_3 AND SUBRULE_1 THEN tax=400.4736842105263                                     | 
| 16 | IF SUBRULE_4 AND SUBRULE_1 THEN tax=437.0                                                 | 
| 17 | IF SUBRULE_7 THEN tax=711.0                                                               | 
| 18 | IF rad > 16.0 THEN tax=666.0              "                                                | 
