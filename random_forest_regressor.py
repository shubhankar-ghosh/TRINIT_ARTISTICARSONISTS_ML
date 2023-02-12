import numpy as np


def model(x, y):

    from sklearn.ensemble import RandomForestRegressor

    regressor = RandomForestRegressor(n_estimators=100, random_state=0)

    regressor.fit(x, y)

    Y_pred = regressor.predict(np.array([6.5]).reshape(1, 1))  # test the output by changing values

    return Y_pred[0]



