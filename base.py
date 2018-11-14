import numpy as np

class BaggingRegressor(object):
    def __init__(self, base_estimator=None, n_estimators=10, max_samples=1.0, verbose=0):
        self.base_estimator = base_estimator
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.verbose = verbose

    def transform(self, X):
        preds = []
        n_obs = X.shape[0]
        n_samples = int(n_obs*self.max_samples)
        for i in range(self.n_estimators):
            rand_idx = np.random.random_integers(low=0, high=n_obs - 1, size=n_samples)
            preds.append(self.base_estimator.transform(X[rand_idx,]))
        return np.mean(preds, axis=0)
