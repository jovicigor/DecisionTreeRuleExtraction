import json
import pandas as pd


def load_rules():
    with open('../data/refactored_rules.json') as f:
        data = json.load(f)
        return data


operator_to_string = {
    'less_or_equal': 'IS LESS OR EQUAL THAN',
    'greater': 'IS GREATER THAN'
}

if __name__ == '__main__':
    config = load_rules()
    rules = config['rules']
    subrules = config['subrules']
    output_variable_name = 'tax'

    human_readable_rules = []
    for subrule in subrules:
        human_readable_rule = subrule['name'] + ': '

        for condition in subrule['conditions']:
            if condition['operator'] == 'between':
                s = f'IF {condition["feature"].strip()} IS IN RANGE ({round(condition["lower_value"], 4)}, {round(condition["higher_value"], 4)}]'
            else:
                s = f'IF {condition["feature"].strip()} {operator_to_string[condition["operator"]]} {round(condition["value"], 4)}'
            if human_readable_rule == f'{subrule["name"]}: ':
                human_readable_rule = human_readable_rule + s
            else:
                human_readable_rule = human_readable_rule + f' AND {s}'

        human_readable_rule = human_readable_rule + f' THEN {subrule["name"]}'
        human_readable_rules.append(human_readable_rule)

    for rule in rules:
        human_readable_rule = ''

        for condition in rule['conditions']:
            if 'subrule' in condition:
                s = f'IF {condition["subrule"]}'
            elif condition['operator'] == 'between':
                s = f'IF {condition["feature"].strip()} IS IN RANGE ({round(condition["lower_value"], 4)}, {round(condition["higher_value"], 4)}]'
            else:
                s = f'IF {condition["feature"].strip()} {operator_to_string[condition["operator"]]} {round(condition["value"], 4)}'
            if human_readable_rule == '':
                human_readable_rule = human_readable_rule + s
            else:
                human_readable_rule = human_readable_rule + f' AND {s}'

        human_readable_rule = human_readable_rule + f' THEN {output_variable_name}={rule["output"]}'

        human_readable_rules.append(human_readable_rule)

    pd.DataFrame({"rules": human_readable_rules}).to_csv('../data/human_readable_rules.csv')
