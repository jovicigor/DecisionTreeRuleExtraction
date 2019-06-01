import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor


def train_decision_tree(df: pd.DataFrame, target_column: str, feature_columns: list):
    scaler = StandardScaler()

    x = df[feature_columns]
    y = df[target_column]

    # x = scaler.fit_transform(x)

    classifier = DecisionTreeRegressor()
    classifier.fit(x, y)
    predict = classifier.predict(x)

    print(f'Accuracy: {accuracy_score(y, predict)}')

    return scaler, classifier
