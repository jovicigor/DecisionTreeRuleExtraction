import numpy as np
from sklearn.tree import _tree


def extract_rules(tree, feature_columns):
    tree_ = tree.tree_
    feature_name = [
        feature_columns[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    pathto = dict()

    global k
    k = 0

    def recurse(node, depth, parent):
        global k

        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            s = "{} <= {} ".format(name, threshold, node)
            if node == 0:
                pathto[node] = s
            else:
                pathto[node] = pathto[parent] + ' & ' + s

            recurse(tree_.children_left[node], depth + 1, node)
            s = "{} > {}".format(name, threshold)
            if node == 0:
                pathto[node] = s
            else:
                pathto[node] = pathto[parent] + ' & ' + s
            recurse(tree_.children_right[node], depth + 1, node)
        else:
            k = k + 1
            value = tree_.value[node][0][0]
            print(k, ')', pathto[parent], value)

    recurse(0, 1, 0)
