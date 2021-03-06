import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor


def train_decision_tree(df: pd.DataFrame, target_column: str, feature_columns: list):
    scaler = StandardScaler()

    x = df[feature_columns]
    y = df[target_column]

    # x = scaler.fit_transform(x)

    classifier = DecisionTreeRegressor(max_depth=5)
    classifier.fit(x, y)
    classifier.predict(x)

    return scaler, classifier
