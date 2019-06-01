import json
import pandas as pd


def load_rules():
    with open('../data/simplified_rules.json') as f:
        data = json.load(f)
        return data


operator_to_string = {
    'less_or_equal': 'IS LESS OR EQUAL THAN',
    'greater': 'IS GREATER THAN'
}

if __name__ == '__main__':
    rules = load_rules()
    output_variable_name = 'tax'

    human_readable_rules = []
    for rule in rules:
        human_readable_rule = ''

        for condition in rule['conditions']:
            s = f'IF {condition["feature"].strip()} {operator_to_string[condition["operator"]]} {round(condition["value"], 4)}'
            if human_readable_rule == '':
                human_readable_rule = human_readable_rule + s
            else:
                human_readable_rule = human_readable_rule + f' AND {s}'

        human_readable_rule = human_readable_rule + f'THEN {output_variable_name} is {rule["output"]}'

        human_readable_rules.append(human_readable_rule)

    pd.DataFrame({"rules": human_readable_rules}).to_csv('../data/human_readable_rules.csv')
