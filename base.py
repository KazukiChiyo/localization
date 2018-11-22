# Author: Kexuan Zou
# Date: Nov 22, 2018

import numpy as np

class Anchor(object):
    def __init__(self, id, coords, rssi_0, rssi=None):
        self.id = id
        self.coords = coords
        self.rssi = rssi
        self.rssi_0 = rssi_0

    def update(self, rssi):
        self.rssi = rssi

    def __str__(self):
        return "Anchor(id: {}, coords: {}, rssi: {})".format(self.id, self.coords, self.rssi)


class Localizer(object):
    def __init__(self, standardize=True):
        """Least square localization algorithm with input standardizer.
        Parameters:
        -----------
        standardize: boolen
            whether to standardize input signals.
        """
        self.standardize = standardize

    def transform(self, X):
        di = []
        for x in X:
            di.append(10**(-.05*(x.rssi - x.rssi_0)))
        x1, y1 = X[0].coords[0], X[0].coords[1]
        x2, y2 = X[1].coords[0], X[1].coords[1]
        x3, y3 = X[2].coords[0], X[2].coords[1]
        H = np.zeros((2, 2))
        H[0, 0], H[0, 1] = 2*(x1 - x3), 2*(y1 - y3)
        H[1, 0], H[1, 1] = 2*(x2 - x3), 2*(y2 - y3)
        y = np.zeros(2)
        y[0] = x1**2 + y1**2 - x3**2 - y3**2 - di[0]**2 + di[2]**2
        y[1] = x2**2 + y2**2 - x3**2 - y3**2 - di[1]**2 + di[2]**2
        return np.linalg.pinv(H).dot(y)


class BaggingRegressor(object):
    def __init__(self, base_estimator=None, n_estimators=10, max_samples=1.0):
        """Unsupervised bootstraping aggregating regressor.
        Parameters:
        -----------
        base_estimator: object
            The base estimator to fit on random subsets of the dataset.
        n_estimators: int
            The number of base estimators in the ensemble.
        max_samples: float
            The proportion of samples to draw from X to train each base estimator.
        """
        self.base_estimator = base_estimator
        self.n_estimators = n_estimators
        self.max_samples = max_samples

    def transform(self, X):
        preds = []
        n_obs = X.shape[0]
        n_samples = int(n_obs*self.max_samples)
        for i in range(self.n_estimators):
            rand_idx = np.random.random_integers(low=0, high=n_obs - 1, size=n_samples)
            preds.append(self.base_estimator.transform(X[rand_idx,]))
        return np.mean(preds, axis=0)
