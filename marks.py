import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def marks_prediction(hrs):
    
    X = pd.read_csv("x.csv", index_col=0)
    y = pd.read_csv("y.csv", index_col=0)

    X = X.values
    y = y.values

    model = LinearRegression()
    model.fit(X, y)

    X_test = np.array(hrs)
    X_test = X_test.reshape(1, -1)

    return model.predict(X_test)[0]
