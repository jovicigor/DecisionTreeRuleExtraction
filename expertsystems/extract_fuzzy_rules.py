import json


def load_rules():
    with open('../data/simplified_rules.json') as f:
        data = json.load(f)
        return data


def extract_ranges(rules):
    conditions = [condition for rule in rules for condition in rule['conditions']]
    features = {condition['feature'] for condition in conditions}
    ranges = []

    for feature in features:
        feature_range = {condition['value'] for condition in conditions if feature == condition['feature']}
        ranges.append({
            'feature': feature,
            'range': sorted(feature_range)
        })

    return ranges


if __name__ == '__main__':
    rules = load_rules()

    ranges = extract_ranges(rules)

    with open('../data/feature_ranges.json', 'w') as outfile:
        json.dump(ranges, outfile)
