import json


def load_rules():
    with open('../data/extracted_rules.json') as f:
        data = json.load(f)
        return data


def simplify_rule(rule):
    conditions = rule['conditions']
    features = {condition['feature'] for condition in rule['conditions']}
    new_conditions = []

    for feature in features:
        feature_conditions = [condition for condition in conditions if condition['feature'] == feature]
        less_or_equal_conditions = [condition for condition in feature_conditions if condition['operator'] == 'less_or_equal']
        greater_conditions = [condition for condition in feature_conditions if condition['operator'] == 'greater']
        less_or_equal_conditions = sorted(less_or_equal_conditions, key=lambda k: k['value'])
        greater_conditions = sorted(greater_conditions, key=lambda k: k['value'], reverse=True)

        if len(less_or_equal_conditions) != 0 and len(greater_conditions) != 0:
            # agregate to between
            between_condition = {
                'feature': feature,
                'operator': 'between',
                'higher_value': less_or_equal_conditions[0]["value"],
                'lower_value': greater_conditions[0]["value"]
            }
            new_conditions.append(between_condition)
        else:
            if len(less_or_equal_conditions) != 0:
                new_conditions.append(less_or_equal_conditions[0])
            if len(greater_conditions) != 0:
                new_conditions.append(greater_conditions[0])

    return {
        'conditions': new_conditions,
        'output': rule['output']
    }


if __name__ == '__main__':
    rules = load_rules()

    simplified_rules = [simplify_rule(rule=rule) for rule in rules]

    with open('../data/simplified_rules.json', 'w') as outfile:
        json.dump(simplified_rules, outfile)
