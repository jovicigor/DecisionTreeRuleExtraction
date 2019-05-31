import numpy as np
from sklearn.tree import _tree


def scale_back(scaler, feature_columns, name, value):
    index = feature_columns.index(name)

    return abs(value * np.sqrt(scaler.var_[index]) + value * scaler.mean_[index])


def extract_rules(tree, feature_columns, scaler):
    tree_ = tree.tree_
    feature_name = [
        feature_columns[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    pathto = dict()

    global k
    k = 0
    rules = []

    def recurse(node, depth, parent):
        global k

        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            threshold = scale_back(scaler, feature_columns, name, threshold)

            if node == 0:
                pathto[node] = []
                pathto[node].append(generate_condition(name, threshold, "less_or_equal"))
            else:
                pathto[node] = pathto[parent] + [generate_condition(name, threshold, "less_or_equal")]

            recurse(tree_.children_left[node], depth + 1, node)

            if node == 0:
                pathto[node] = []
                pathto[node].append(generate_condition(name, threshold, "greater"))
            else:
                pathto[node] = pathto[parent] + [generate_condition(name, threshold, "greater")]

            recurse(tree_.children_right[node], depth + 1, node)
        else:
            k = k + 1
            value = tree_.value[node][0][0]
            rules.append({
                "conditions": pathto[parent],
                "output": value
            })

    recurse(0, 1, 0)
    return rules


def generate_condition(feature, value, operator):
    return {
        "feature": feature,
        "operator": operator,
        "value": value
    }
