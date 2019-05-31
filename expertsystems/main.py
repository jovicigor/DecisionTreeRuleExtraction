import json

import pandas as pd

from rule_miner import extract_rules
from trainer import train_decision_tree

if __name__ == '__main__':
    df = pd.read_csv('../data/boston_housing.csv')
    target_column = 'tax'
    feature_columns = [column for column in list(df) if column != target_column]

    scaler, classifier = train_decision_tree(df=df, target_column=target_column, feature_columns=feature_columns)

    rules = extract_rules(classifier, feature_columns=feature_columns)

    with open('../data/extracted_rules.json', 'w') as outfile:
        json.dump(rules, outfile)
