from sklearn.linear_model import LogisticRegression
import numpy as np

class MakerTakerModel:
    def __init__(self):
        self.model = LogisticRegression()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, features):
        return self.model.predict_proba([features])[0][1]  # Probability of taker