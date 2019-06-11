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
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| 0   | SUBRULE_0: IF rad IS IN RANGE (3.5, 16.0] AND IF dis IS GREATER THAN 2.8589 THEN SUBRULE_0                                                                                                                                                       | 
| 1   | SUBRULE_1: IF indus IS LESS OR EQUAL THAN 26.695 AND IF rad IS LESS OR EQUAL THAN 3.5 THEN SUBRULE_1                                                                                                                                               | 
| 2   | SUBRULE_2: IF crim IS GREATER THAN 0.043 AND IF nox IS LESS OR EQUAL THAN 0.438 THEN SUBRULE_2                                                                                                                                                     | 
| 3   | SUBRULE_3: IF indus IS LESS OR EQUAL THAN 26.695 AND IF nox IS LESS OR EQUAL THAN 0.438 THEN SUBRULE_3                                                                                                                                             | 
| 4   | SUBRULE_4: IF ptratio IS LESS OR EQUAL THAN 20.4 AND IF nox IS LESS OR EQUAL THAN 0.48 THEN SUBRULE_4                                                                                                                                              | 
| 5   | SUBRULE_5: IF rad IS IN RANGE (3.5, 16.0] AND IF crim IS GREATER THAN 0.0628 THEN SUBRULE_5                                                                                                                                                      | 
| 6   | SUBRULE_6: IF crim IS LESS OR EQUAL THAN 0.0628 AND IF b IS GREATER THAN 372.82 THEN SUBRULE_6                                                                                                                                                     | 
| 7   | SUBRULE_7: IF indus IS IN RANGE (4.15, 26.695] AND IF dis IS IN RANGE (5.0654, 6.4171] THEN SUBRULE_7                                                                                                                                            | 
| 8   | SUBRULE_8: IF age IS LESS OR EQUAL THAN 38.35 AND IF zn IS LESS OR EQUAL THAN 90.0 THEN SUBRULE_8                                                                                                                                                  | 
| 9   | SUBRULE_9: IF lstat IS GREATER THAN 3.365 AND IF indus IS LESS OR EQUAL THAN 26.695 THEN SUBRULE_9                                                                                                                                                 | 
| 10  | SUBRULE_10: IF age IS GREATER THAN 17.35 AND IF crim IS LESS OR EQUAL THAN 0.0201 THEN SUBRULE_10                                                                                                                                                  | 
| 11  | SUBRULE_11: IF crim IS GREATER THAN 0.0201 AND IF dis IS GREATER THAN 6.2433 THEN SUBRULE_11                                                                                                                                                       | 
| 12  | SUBRULE_12: IF zn IS LESS OR EQUAL THAN 82.5 AND IF medv IS LESS OR EQUAL THAN 26.35 THEN SUBRULE_12                                                                                                                                               | 
| 13  | SUBRULE_13: IF ptratio IS GREATER THAN 17.85 AND IF rad IS IN RANGE (2.5, 3.5] THEN SUBRULE_13                                                                                                                                                   | 
| 14  | SUBRULE_14: IF rad IS IN RANGE (3.5, 16.0] AND IF dis IS GREATER THAN 5.0654 THEN SUBRULE_14                                                                                                                                                     | 
| 15  | SUBRULE_15: IF nox IS IN RANGE (0.438, 0.583] AND IF dis IS IN RANGE (2.8589, 6.8166] THEN SUBRULE_15                                                                                                                                            | 
| 16  | SUBRULE_16: IF dis IS LESS OR EQUAL THAN 2.8589 AND IF rad IS IN RANGE (3.5, 16.0] THEN SUBRULE_16                                                                                                                                               | 
| 17  | IF nox IS LESS OR EQUAL THAN 0.577 AND IF lstat IS LESS OR EQUAL THAN 3.365 AND IF dis IS LESS OR EQUAL THAN 6.2433 AND IF rad IS LESS OR EQUAL THAN 2.5 AND IF indus IS LESS OR EQUAL THAN 26.695 THEN tax=198.0                                  | 
| 18  | IF SUBRULE_9 AND IF nox IS LESS OR EQUAL THAN 0.467 AND IF dis IS LESS OR EQUAL THAN 3.7926 AND IF rad IS LESS OR EQUAL THAN 2.5 THEN tax=276.0                                                                                                    | 
| 19  | IF SUBRULE_9 AND IF rad IS LESS OR EQUAL THAN 1.5 AND IF dis IS LESS OR EQUAL THAN 3.7926 AND IF nox IS IN RANGE (0.467, 0.577] THEN tax=273.0                                                                                                   | 
| 20  | IF SUBRULE_9 AND IF rad IS IN RANGE (1.5, 2.5] AND IF dis IS LESS OR EQUAL THAN 3.7926 AND IF nox IS IN RANGE (0.467, 0.577] THEN tax=270.0                                                                                                      | 
| 21  | IF SUBRULE_9 AND IF dis IS IN RANGE (3.7926, 4.5286] AND IF nox IS LESS OR EQUAL THAN 0.577 AND IF rad IS LESS OR EQUAL THAN 2.5 THEN tax=296.0                                                                                                  | 
| 22  | IF SUBRULE_9 AND IF nox IS LESS OR EQUAL THAN 0.577 AND IF age IS LESS OR EQUAL THAN 39.95 AND IF rad IS LESS OR EQUAL THAN 2.5 AND IF dis IS IN RANGE (4.5286, 6.2433] THEN tax=265.0                                                           | 
| 23  | IF SUBRULE_9 AND IF nox IS LESS OR EQUAL THAN 0.577 AND IF age IS GREATER THAN 39.95 AND IF rad IS LESS OR EQUAL THAN 2.5 AND IF dis IS IN RANGE (4.5286, 6.2433] THEN tax=242.0                                                                 | 
| 24  | IF nox IS LESS OR EQUAL THAN 0.577 AND IF ptratio IS LESS OR EQUAL THAN 17.85 AND IF dis IS LESS OR EQUAL THAN 6.2433 AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF rad IS IN RANGE (2.5, 3.5] THEN tax=193.0                                 | 
| 25  | IF SUBRULE_13 AND IF nox IS LESS OR EQUAL THAN 0.4535 AND IF dis IS LESS OR EQUAL THAN 5.0903 AND IF indus IS LESS OR EQUAL THAN 5.7 THEN tax=247.0                                                                                                | 
| 26  | IF SUBRULE_13 AND IF nox IS LESS OR EQUAL THAN 0.4535 AND IF indus IS LESS OR EQUAL THAN 5.7 AND IF dis IS IN RANGE (5.0903, 6.2433] THEN tax=252.0                                                                                              | 
| 27  | IF SUBRULE_13 AND IF nox IS LESS OR EQUAL THAN 0.4535 AND IF indus IS IN RANGE (5.7, 26.695] AND IF dis IS LESS OR EQUAL THAN 6.2433 THEN tax=233.0                                                                                              | 
| 28  | IF SUBRULE_13 AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF dis IS LESS OR EQUAL THAN 6.2433 AND IF nox IS IN RANGE (0.4535, 0.461] THEN tax=222.0                                                                                            | 
| 29  | IF SUBRULE_13 AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF dis IS LESS OR EQUAL THAN 6.2433 AND IF nox IS IN RANGE (0.461, 0.577] THEN tax=223.0                                                                                             | 
| 30  | IF SUBRULE_1 AND IF dis IS LESS OR EQUAL THAN 6.2433 AND IF nox IS IN RANGE (0.577, 0.583] THEN tax=188.0                                                                                                                                        | 
| 31  | IF SUBRULE_1 AND IF nox IS LESS OR EQUAL THAN 0.583 AND IF crim IS LESS OR EQUAL THAN 0.0201 AND IF age IS LESS OR EQUAL THAN 17.35 AND IF ptratio IS LESS OR EQUAL THAN 20.4 AND IF dis IS GREATER THAN 6.2433 THEN tax=402.0                     | 
| 32  | IF SUBRULE_1 AND IF SUBRULE_10 AND IF lstat IS LESS OR EQUAL THAN 8.04 AND IF nox IS LESS OR EQUAL THAN 0.583 AND IF ptratio IS LESS OR EQUAL THAN 15.7 AND IF dis IS IN RANGE (6.2433, 7.1726] THEN tax=284.0                                   | 
| 33  | IF SUBRULE_1 AND IF SUBRULE_10 AND IF lstat IS LESS OR EQUAL THAN 8.04 AND IF nox IS LESS OR EQUAL THAN 0.583 AND IF ptratio IS LESS OR EQUAL THAN 15.7 AND IF dis IS GREATER THAN 7.1726 THEN tax=285.0                                           | 
| 34  | IF SUBRULE_1 AND IF SUBRULE_10 AND IF nox IS LESS OR EQUAL THAN 0.583 AND IF ptratio IS LESS OR EQUAL THAN 15.7 AND IF lstat IS GREATER THAN 8.04 AND IF dis IS GREATER THAN 6.2433 THEN tax=300.0                                                 | 
| 35  | IF SUBRULE_1 AND IF SUBRULE_10 AND IF nox IS LESS OR EQUAL THAN 0.3895 AND IF ptratio IS IN RANGE (15.7, 18.4] AND IF dis IS GREATER THAN 6.2433 THEN tax=241.0                                                                                  | 
| 36  | IF SUBRULE_1 AND IF SUBRULE_10 AND IF ptratio IS IN RANGE (15.7, 18.4] AND IF nox IS IN RANGE (0.3895, 0.583] AND IF dis IS GREATER THAN 6.2433 THEN tax=244.0                                                                                   | 
| 37  | IF SUBRULE_1 AND IF SUBRULE_10 AND IF nox IS LESS OR EQUAL THAN 0.583 AND IF ptratio IS IN RANGE (18.4, 20.4] AND IF dis IS GREATER THAN 6.2433 THEN tax=216.0                                                                                   | 
| 38  | IF SUBRULE_4 AND IF SUBRULE_1 AND IF SUBRULE_8 AND IF rm IS LESS OR EQUAL THAN 6.661 AND IF dis IS IN RANGE (6.2433, 7.9141] AND IF crim IS GREATER THAN 0.0201 THEN tax=304.0                                                                   | 
| 39  | IF SUBRULE_4 AND IF SUBRULE_1 AND IF SUBRULE_8 AND IF rm IS LESS OR EQUAL THAN 6.661 AND IF dis IS IN RANGE (7.9141, 9.2039] AND IF crim IS GREATER THAN 0.0201 THEN tax=313.0                                                                   | 
| 40  | IF SUBRULE_4 AND IF SUBRULE_1 AND IF SUBRULE_8 AND IF dis IS GREATER THAN 9.2039 AND IF rm IS LESS OR EQUAL THAN 6.661 AND IF crim IS GREATER THAN 0.0201 THEN tax=315.0                                                                           | 
| 41  | IF SUBRULE_4 AND IF SUBRULE_1 AND IF SUBRULE_8 AND IF crim IS IN RANGE (0.0201, 0.0254] AND IF rm IS GREATER THAN 6.661 AND IF dis IS GREATER THAN 6.2433 THEN tax=348.0                                                                         | 
| 42  | IF SUBRULE_4 AND IF SUBRULE_8 AND IF rad IS LESS OR EQUAL THAN 1.5 AND IF rm IS GREATER THAN 6.661 AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF crim IS GREATER THAN 0.0254 AND IF dis IS GREATER THAN 6.2433 THEN tax=335.0                   | 
| 43  | IF SUBRULE_4 AND IF SUBRULE_8 AND IF rad IS IN RANGE (1.5, 3.5] AND IF rm IS GREATER THAN 6.661 AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF crim IS GREATER THAN 0.0254 AND IF dis IS GREATER THAN 6.2433 THEN tax=329.0                    | 
| 44  | IF SUBRULE_4 AND IF SUBRULE_1 AND IF SUBRULE_11 AND IF age IS GREATER THAN 38.35 AND IF zn IS LESS OR EQUAL THAN 90.0 AND IF lstat IS LESS OR EQUAL THAN 6.705 THEN tax=335.0                                                                      | 
| 45  | IF SUBRULE_4 AND IF SUBRULE_1 AND IF SUBRULE_11 AND IF age IS GREATER THAN 38.35 AND IF zn IS LESS OR EQUAL THAN 90.0 AND IF b IS LESS OR EQUAL THAN 389.705 AND IF lstat IS GREATER THAN 6.705 THEN tax=352.0                                     | 
| 46  | IF SUBRULE_4 AND IF SUBRULE_1 AND IF SUBRULE_11 AND IF b IS GREATER THAN 389.705 AND IF age IS GREATER THAN 38.35 AND IF zn IS LESS OR EQUAL THAN 90.0 AND IF lstat IS GREATER THAN 6.705 THEN tax=348.0                                           | 
| 47  | IF SUBRULE_11 AND IF SUBRULE_1 AND IF SUBRULE_4 AND IF zn IS GREATER THAN 90.0 THEN tax=402.0                                                                                                                                                      | 
| 48  | IF SUBRULE_11 AND IF SUBRULE_1 AND IF ptratio IS LESS OR EQUAL THAN 20.4 AND IF nox IS IN RANGE (0.48, 0.583] THEN tax=422.0                                                                                                                     | 
| 49  | IF SUBRULE_1 AND IF ptratio IS GREATER THAN 20.4 AND IF nox IS LESS OR EQUAL THAN 0.583 AND IF dis IS GREATER THAN 6.2433 THEN tax=469.0                                                                                                           | 
| 50  | IF SUBRULE_16 AND IF nox IS LESS OR EQUAL THAN 0.583 AND IF indus IS LESS OR EQUAL THAN 4.01 AND IF ptratio IS LESS OR EQUAL THAN 19.65 THEN tax=264.0                                                                                             | 
| 51  | IF SUBRULE_16 AND IF nox IS LESS OR EQUAL THAN 0.527 AND IF indus IS IN RANGE (4.01, 9.955] AND IF ptratio IS LESS OR EQUAL THAN 19.65 THEN tax=296.0                                                                                            | 
| 52  | IF SUBRULE_16 AND IF indus IS IN RANGE (4.01, 9.955] AND IF nox IS IN RANGE (0.527, 0.583] AND IF ptratio IS LESS OR EQUAL THAN 19.65 THEN tax=304.0                                                                                             | 
| 53  | IF SUBRULE_16 AND IF indus IS LESS OR EQUAL THAN 9.955 AND IF nox IS LESS OR EQUAL THAN 0.583 AND IF ptratio IS GREATER THAN 19.65 THEN tax=384.0                                                                                                  | 
| 54  | IF SUBRULE_16 AND IF nox IS LESS OR EQUAL THAN 0.583 AND IF indus IS IN RANGE (9.955, 26.695] THEN tax=432.0                                                                                                                                     | 
| 55  | IF SUBRULE_12 AND IF SUBRULE_3 AND IF SUBRULE_0 AND IF crim IS LESS OR EQUAL THAN 0.043 AND IF age IS LESS OR EQUAL THAN 29.1 AND IF ptratio IS LESS OR EQUAL THAN 16.35 THEN tax=337.0                                                            | 
| 56  | IF SUBRULE_12 AND IF SUBRULE_3 AND IF SUBRULE_0 AND IF crim IS LESS OR EQUAL THAN 0.043 AND IF ptratio IS LESS OR EQUAL THAN 16.35 AND IF age IS GREATER THAN 29.1 THEN tax=329.0                                                                  | 
| 57  | IF SUBRULE_12 AND IF SUBRULE_3 AND IF SUBRULE_0 AND IF ptratio IS GREATER THAN 16.35 AND IF crim IS LESS OR EQUAL THAN 0.0377 AND IF age IS LESS OR EQUAL THAN 30.95 THEN tax=280.0                                                                | 
| 58  | IF SUBRULE_12 AND IF SUBRULE_3 AND IF SUBRULE_0 AND IF ptratio IS GREATER THAN 16.35 AND IF age IS GREATER THAN 30.95 AND IF crim IS LESS OR EQUAL THAN 0.0377 THEN tax=281.0                                                                      | 
| 59  | IF SUBRULE_12 AND IF SUBRULE_3 AND IF SUBRULE_0 AND IF crim IS IN RANGE (0.0377, 0.043] AND IF ptratio IS GREATER THAN 16.35 THEN tax=293.0                                                                                                      | 
| 60  | IF SUBRULE_3 AND IF SUBRULE_0 AND IF zn IS GREATER THAN 82.5 AND IF crim IS LESS OR EQUAL THAN 0.043 AND IF medv IS LESS OR EQUAL THAN 26.35 THEN tax=351.0                                                                                        | 
| 61  | IF SUBRULE_3 AND IF SUBRULE_0 AND IF medv IS GREATER THAN 26.35 AND IF b IS LESS OR EQUAL THAN 392.84 AND IF age IS LESS OR EQUAL THAN 34.65 AND IF crim IS LESS OR EQUAL THAN 0.043 THEN tax=224.0                                                | 
| 62  | IF SUBRULE_3 AND IF SUBRULE_0 AND IF medv IS GREATER THAN 26.35 AND IF b IS LESS OR EQUAL THAN 392.84 AND IF crim IS LESS OR EQUAL THAN 0.043 AND IF age IS GREATER THAN 34.65 THEN tax=187.0                                                      | 
| 63  | IF SUBRULE_3 AND IF SUBRULE_0 AND IF medv IS GREATER THAN 26.35 AND IF b IS IN RANGE (392.84, 393.565] AND IF crim IS LESS OR EQUAL THAN 0.0386 AND IF lstat IS LESS OR EQUAL THAN 4.755 THEN tax=256.0                                          | 
| 64  | IF SUBRULE_3 AND IF SUBRULE_0 AND IF b IS IN RANGE (393.565, 395.565] AND IF medv IS GREATER THAN 26.35 AND IF lstat IS LESS OR EQUAL THAN 4.755 AND IF crim IS LESS OR EQUAL THAN 0.0386 THEN tax=255.0                                         | 
| 65  | IF SUBRULE_3 AND IF SUBRULE_0 AND IF medv IS GREATER THAN 26.35 AND IF lstat IS LESS OR EQUAL THAN 4.755 AND IF crim IS LESS OR EQUAL THAN 0.0386 AND IF b IS GREATER THAN 395.565 THEN tax=245.0                                                  | 
| 66  | IF SUBRULE_3 AND IF SUBRULE_0 AND IF medv IS GREATER THAN 26.35 AND IF crim IS LESS OR EQUAL THAN 0.0386 AND IF b IS GREATER THAN 392.84 AND IF lstat IS GREATER THAN 4.755 THEN tax=226.0                                                         | 
| 67  | IF SUBRULE_3 AND IF SUBRULE_0 AND IF crim IS IN RANGE (0.0386, 0.043] AND IF medv IS GREATER THAN 26.35 AND IF b IS GREATER THAN 392.84 THEN tax=281.0                                                                                           | 
| 68  | IF SUBRULE_2 AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF dis IS IN RANGE (2.8589, 5.0654] AND IF rad IS IN RANGE (3.5, 16.0] THEN tax=398.0                                                                                                 | 
| 69  | IF SUBRULE_14 AND IF SUBRULE_2 AND IF indus IS LESS OR EQUAL THAN 2.565 AND IF zn IS LESS OR EQUAL THAN 65.0 THEN tax=411.0                                                                                                                        | 
| 70  | IF SUBRULE_14 AND IF SUBRULE_2 AND IF indus IS IN RANGE (2.565, 4.15] AND IF zn IS LESS OR EQUAL THAN 65.0 THEN tax=398.0                                                                                                                        | 
| 71  | IF SUBRULE_2 AND IF SUBRULE_14 AND IF rm IS LESS OR EQUAL THAN 6.1405 AND IF b IS LESS OR EQUAL THAN 389.85 AND IF indus IS LESS OR EQUAL THAN 4.15 AND IF zn IS GREATER THAN 65.0 THEN tax=334.0                                                  | 
| 72  | IF SUBRULE_2 AND IF SUBRULE_14 AND IF b IS GREATER THAN 389.85 AND IF rm IS LESS OR EQUAL THAN 6.1405 AND IF indus IS LESS OR EQUAL THAN 4.15 AND IF zn IS GREATER THAN 65.0 THEN tax=337.0                                                        | 
| 73  | IF SUBRULE_2 AND IF SUBRULE_14 AND IF indus IS LESS OR EQUAL THAN 4.15 AND IF rm IS GREATER THAN 6.1405 AND IF zn IS GREATER THAN 65.0 THEN tax=358.0                                                                                              | 
| 74  | IF SUBRULE_7 AND IF nox IS LESS OR EQUAL THAN 0.4205 AND IF b IS LESS OR EQUAL THAN 392.05 AND IF medv IS LESS OR EQUAL THAN 35.2 AND IF rad IS IN RANGE (3.5, 6.5] AND IF crim IS GREATER THAN 0.043 THEN tax=305.0                             | 
| 75  | IF SUBRULE_7 AND IF b IS LESS OR EQUAL THAN 392.05 AND IF medv IS LESS OR EQUAL THAN 35.2 AND IF rad IS IN RANGE (3.5, 6.5] AND IF nox IS IN RANGE (0.4205, 0.438] AND IF crim IS GREATER THAN 0.043 THEN tax=300.0                              | 
| 76  | IF SUBRULE_2 AND IF SUBRULE_7 AND IF medv IS LESS OR EQUAL THAN 20.2 AND IF rad IS IN RANGE (3.5, 6.5] AND IF b IS GREATER THAN 392.05 THEN tax=300.0                                                                                            | 
| 77  | IF SUBRULE_2 AND IF SUBRULE_7 AND IF medv IS IN RANGE (20.2, 35.2] AND IF rad IS IN RANGE (3.5, 6.5] AND IF ptratio IS LESS OR EQUAL THAN 17.5 AND IF b IS GREATER THAN 392.05 THEN tax=289.0                                                    | 
| 78  | IF SUBRULE_2 AND IF SUBRULE_7 AND IF medv IS IN RANGE (20.2, 35.2] AND IF rad IS IN RANGE (3.5, 6.5] AND IF b IS GREATER THAN 392.05 AND IF ptratio IS GREATER THAN 17.5 THEN tax=281.0                                                          | 
| 79  | IF SUBRULE_2 AND IF SUBRULE_7 AND IF rad IS IN RANGE (6.5, 16.0] AND IF medv IS LESS OR EQUAL THAN 35.2 THEN tax=329.0                                                                                                                           | 
| 80  | IF SUBRULE_2 AND IF SUBRULE_7 AND IF medv IS GREATER THAN 35.2 AND IF rad IS IN RANGE (3.5, 16.0] THEN tax=245.0                                                                                                                                 | 
| 81  | IF SUBRULE_2 AND IF indus IS IN RANGE (4.15, 5.965] AND IF rad IS IN RANGE (3.5, 16.0] AND IF zn IS LESS OR EQUAL THAN 26.0 AND IF dis IS GREATER THAN 6.4171 THEN tax=330.0                                                                     | 
| 82  | IF SUBRULE_2 AND IF indus IS IN RANGE (5.965, 26.695] AND IF rad IS IN RANGE (3.5, 16.0] AND IF zn IS LESS OR EQUAL THAN 26.0 AND IF dis IS GREATER THAN 6.4171 THEN tax=345.0                                                                   | 
| 83  | IF SUBRULE_2 AND IF zn IS GREATER THAN 26.0 AND IF indus IS IN RANGE (4.15, 5.125] AND IF rad IS IN RANGE (3.5, 16.0] AND IF dis IS GREATER THAN 6.4171 THEN tax=300.0                                                                           | 
| 84  | IF SUBRULE_2 AND IF zn IS GREATER THAN 26.0 AND IF indus IS IN RANGE (5.125, 26.695] AND IF rad IS IN RANGE (3.5, 16.0] AND IF dis IS GREATER THAN 6.4171 THEN tax=293.0                                                                         | 
| 85  | IF SUBRULE_0 AND IF b IS LESS OR EQUAL THAN 372.82 AND IF crim IS LESS OR EQUAL THAN 0.0628 AND IF nox IS IN RANGE (0.438, 0.583] AND IF indus IS LESS OR EQUAL THAN 26.695 THEN tax=430.0                                                       | 
| 86  | IF SUBRULE_6 AND IF SUBRULE_0 AND IF zn IS LESS OR EQUAL THAN 47.5 AND IF indus IS LESS OR EQUAL THAN 6.025 AND IF nox IS IN RANGE (0.438, 0.441] AND IF age IS LESS OR EQUAL THAN 71.85 THEN tax=243.0                                          | 
| 87  | IF SUBRULE_6 AND IF SUBRULE_0 AND IF lstat IS LESS OR EQUAL THAN 5.135 AND IF zn IS LESS OR EQUAL THAN 47.5 AND IF indus IS LESS OR EQUAL THAN 6.025 AND IF nox IS IN RANGE (0.441, 0.583] AND IF age IS LESS OR EQUAL THAN 71.85 THEN tax=216.0 | 
| 88  | IF SUBRULE_6 AND IF SUBRULE_0 AND IF zn IS LESS OR EQUAL THAN 16.5 AND IF indus IS LESS OR EQUAL THAN 6.025 AND IF lstat IS GREATER THAN 5.135 AND IF nox IS IN RANGE (0.441, 0.583] AND IF age IS LESS OR EQUAL THAN 71.85 THEN tax=224.0       | 
| 89  | IF SUBRULE_6 AND IF SUBRULE_0 AND IF indus IS LESS OR EQUAL THAN 6.025 AND IF lstat IS GREATER THAN 5.135 AND IF nox IS IN RANGE (0.441, 0.583] AND IF age IS LESS OR EQUAL THAN 71.85 AND IF zn IS IN RANGE (16.5, 47.5] THEN tax=222.0         | 
| 90  | IF SUBRULE_6 AND IF SUBRULE_0 AND IF zn IS LESS OR EQUAL THAN 47.5 AND IF age IS GREATER THAN 71.85 AND IF indus IS LESS OR EQUAL THAN 6.025 AND IF nox IS IN RANGE (0.438, 0.583] THEN tax=296.0                                                | 
| 91  | IF SUBRULE_6 AND IF SUBRULE_0 AND IF indus IS IN RANGE (6.025, 26.695] AND IF zn IS LESS OR EQUAL THAN 47.5 AND IF chas IS LESS OR EQUAL THAN 0.5 AND IF nox IS IN RANGE (0.438, 0.583] AND IF medv IS LESS OR EQUAL THAN 28.7 THEN tax=270.0    | 
| 92  | IF SUBRULE_6 AND IF SUBRULE_0 AND IF indus IS IN RANGE (6.025, 26.695] AND IF chas IS GREATER THAN 0.5 AND IF zn IS LESS OR EQUAL THAN 47.5 AND IF nox IS IN RANGE (0.438, 0.583] AND IF medv IS LESS OR EQUAL THAN 28.7 THEN tax=276.0          | 
| 93  | IF SUBRULE_6 AND IF SUBRULE_0 AND IF indus IS IN RANGE (6.025, 26.695] AND IF zn IS LESS OR EQUAL THAN 47.5 AND IF medv IS GREATER THAN 28.7 AND IF nox IS IN RANGE (0.438, 0.583] THEN tax=254.0                                                | 
| 94  | IF SUBRULE_6 AND IF SUBRULE_0 AND IF zn IS GREATER THAN 47.5 AND IF nox IS IN RANGE (0.438, 0.583] AND IF indus IS LESS OR EQUAL THAN 26.695 THEN tax=370.0                                                                                      | 
| 95  | IF SUBRULE_0 AND IF zn IS LESS OR EQUAL THAN 16.25 AND IF nox IS IN RANGE (0.438, 0.4745] AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF crim IS GREATER THAN 0.0628 THEN tax=430.0                                                            | 
| 96  | IF SUBRULE_5 AND IF dis IS IN RANGE (2.8589, 4.4476] AND IF zn IS LESS OR EQUAL THAN 16.25 AND IF nox IS IN RANGE (0.4745, 0.5015] AND IF indus IS LESS OR EQUAL THAN 8.275 THEN tax=279.0                                                       | 
| 97  | IF SUBRULE_5 AND IF dis IS IN RANGE (2.8589, 4.4476] AND IF zn IS LESS OR EQUAL THAN 16.25 AND IF indus IS IN RANGE (8.275, 26.695] AND IF nox IS IN RANGE (0.4745, 0.5015] THEN tax=277.0                                                       | 
| 98  | IF SUBRULE_5 AND IF zn IS LESS OR EQUAL THAN 16.25 AND IF nox IS IN RANGE (0.4745, 0.5015] AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF dis IS GREATER THAN 4.4476 THEN tax=287.0                                                            | 
| 99  | IF SUBRULE_0 AND IF zn IS LESS OR EQUAL THAN 16.25 AND IF indus IS LESS OR EQUAL THAN 5.125 AND IF nox IS IN RANGE (0.5015, 0.547] AND IF crim IS GREATER THAN 0.0628 THEN tax=296.0                                                             | 
| 100 | IF SUBRULE_0 AND IF crim IS IN RANGE (0.0628, 0.2351] AND IF zn IS LESS OR EQUAL THAN 16.25 AND IF indus IS IN RANGE (5.125, 26.695] AND IF nox IS IN RANGE (0.5015, 0.547] THEN tax=311.0                                                       | 
| 101 | IF SUBRULE_0 AND IF zn IS LESS OR EQUAL THAN 16.25 AND IF indus IS IN RANGE (5.125, 26.695] AND IF nox IS IN RANGE (0.5015, 0.541] AND IF crim IS GREATER THAN 0.2351 THEN tax=307.0                                                             | 
| 102 | IF SUBRULE_0 AND IF zn IS LESS OR EQUAL THAN 16.25 AND IF indus IS IN RANGE (5.125, 26.695] AND IF nox IS IN RANGE (0.541, 0.547] AND IF crim IS GREATER THAN 0.2351 THEN tax=304.0                                                              | 
| 103 | IF SUBRULE_0 AND IF zn IS LESS OR EQUAL THAN 16.25 AND IF nox IS IN RANGE (0.547, 0.583] AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF crim IS GREATER THAN 0.0628 THEN tax=276.0                                                             | 
| 104 | IF SUBRULE_15 AND IF SUBRULE_5 AND IF medv IS LESS OR EQUAL THAN 34.25 AND IF indus IS LESS OR EQUAL THAN 3.65 AND IF zn IS GREATER THAN 16.25 THEN tax=222.0                                                                                      | 
| 105 | IF SUBRULE_15 AND IF SUBRULE_5 AND IF medv IS GREATER THAN 34.25 AND IF indus IS LESS OR EQUAL THAN 3.65 AND IF zn IS GREATER THAN 16.25 THEN tax=216.0                                                                                            | 
| 106 | IF SUBRULE_15 AND IF SUBRULE_5 AND IF rm IS LESS OR EQUAL THAN 6.2225 AND IF indus IS IN RANGE (3.65, 26.695] AND IF zn IS GREATER THAN 16.25 THEN tax=243.0                                                                                     | 
| 107 | IF SUBRULE_15 AND IF SUBRULE_5 AND IF indus IS IN RANGE (3.65, 26.695] AND IF rm IS GREATER THAN 6.2225 AND IF zn IS IN RANGE (16.25, 30.0] THEN tax=264.0                                                                                       | 
| 108 | IF SUBRULE_15 AND IF SUBRULE_5 AND IF indus IS IN RANGE (3.65, 26.695] AND IF rm IS GREATER THAN 6.2225 AND IF zn IS GREATER THAN 30.0 THEN tax=254.0                                                                                            | 
| 109 | IF SUBRULE_5 AND IF nox IS IN RANGE (0.438, 0.583] AND IF indus IS LESS OR EQUAL THAN 26.695 AND IF zn IS GREATER THAN 16.25 AND IF dis IS GREATER THAN 6.8166 THEN tax=284.0                                                                    | 
| 110 | IF indus IS LESS OR EQUAL THAN 26.695 AND IF nox IS GREATER THAN 0.583 AND IF ptratio IS LESS OR EQUAL THAN 13.85 AND IF rad IS LESS OR EQUAL THAN 16.0 THEN tax=264.0                                                                             | 
| 111 | IF nox IS GREATER THAN 0.583 AND IF ptratio IS GREATER THAN 13.85 AND IF indus IS LESS OR EQUAL THAN 14.635 AND IF rad IS LESS OR EQUAL THAN 16.0 THEN tax=391.0                                                                                   | 
| 112 | IF nox IS GREATER THAN 0.583 AND IF ptratio IS GREATER THAN 13.85 AND IF indus IS IN RANGE (14.635, 20.735] AND IF rad IS LESS OR EQUAL THAN 16.0 THEN tax=403.0                                                                                 | 
| 113 | IF indus IS IN RANGE (20.735, 26.695] AND IF nox IS GREATER THAN 0.583 AND IF ptratio IS GREATER THAN 13.85 AND IF rad IS LESS OR EQUAL THAN 16.0 THEN tax=437.0                                                                                 | 
| 114 | IF indus IS GREATER THAN 26.695 AND IF rad IS LESS OR EQUAL THAN 16.0 THEN tax=711.0                                                                                                                                                               | 
| 115 | IF rad IS GREATER THAN 16.0 THEN tax=666.0                                                                                                                                                                                                         | 
