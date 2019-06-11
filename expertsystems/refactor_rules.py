import itertools
import json


def load_rules():
    with open('../data/simplified_rules.json') as f:
        data = json.load(f)
        return data


def generate_combos(rules):
    conditions = {frozenset(condition.items()) for rule in rules for condition in rule['conditions']}

    all_combos = set()
    combinations = itertools.combinations(conditions, 2)
    for index, subset in enumerate(combinations):
        all_combos.add(frozenset({
                                     'combo_id': index,
                                     'combination': subset,
                                 }.items()))

    relevant_combos = set()
    for rule in rules:
        for combo in all_combos:
            combo_dict = dict(combo)
            if len(set(combo_dict['combination'])) > 1 and set(combo_dict['combination']).issubset(
                    {frozenset(condition.items()) for condition in rule['conditions']}):
                relevant_combos.add(combo)

    return relevant_combos


if __name__ == '__main__':
    rules = load_rules()
    combinations = generate_combos(rules)
    refactored_rules = {
        'subrules': [],
        'rules': rules
    }
    initial_num = len(combinations)
    subrule_index = 0
    while len(combinations) > 0:
        print(f'Done: {(initial_num - len(combinations)) / initial_num}')

        counts = {}
        for combo in combinations:
            number = 0
            combo = dict(combo)
            for rule in refactored_rules['rules']:
                if set(combo['combination']).issubset({frozenset(condition.items()) for condition in rule['conditions']}):
                    number += 1

            counts[combo['combo_id']] = number

        combo_id = sorted(counts.items(), key=lambda k: k[1])[-1]
        if combo_id[1] < 0.05 * len(rules):
            combinations = [combination for combination in combinations if dict(combination)['combo_id'] != combo_id[0]]
            break
        else:
            combo_id = combo_id[0]
        subrule = [combination for combination in combinations if dict(combination)['combo_id'] == combo_id][0]
        subrule_name = f'SUBRULE_{subrule_index}'

        new_rules = []
        for rule in refactored_rules['rules']:
            rule_conditions = {frozenset(condition.items()) for condition in rule['conditions']}
            subrule_conditions = set(dict(subrule)['combination'])

            new_conditions = rule_conditions
            if rule_conditions.issuperset(subrule_conditions):
                for item in subrule_conditions:
                    new_conditions.remove(item)
                new_conditions.add(frozenset({'subrule': subrule_name}.items()))

            new_rules.append({
                'conditions': sorted([dict(condition) for condition in new_conditions], key=lambda k: 0 if 'subrule' in k else 1),
                'output': rule['output']
            })

            assert len(rule['conditions'])

        refactored_rules['rules'] = new_rules
        refactored_rules['subrules'].append({
            'name': subrule_name,
            'conditions': [dict(condition) for condition in dict(subrule)['combination']]
        })

        combinations = [combination for combination in combinations if dict(combination)['combo_id'] != combo_id]
        subrule_index += 1

    with open('../data/refactored_rules.json', 'w') as outfile:
        json.dump(refactored_rules, outfile)

# TODO:
# - find all combinations of two and number of times they occure
# - pick one
# - apply changes
# - repeat until no more rules
