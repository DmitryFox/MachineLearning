import numpy as np


class PCA:
    def __init__(self, k):
        self.k = k
        self.w = np.array([])
        self.mu = 0

    def fit(self, x):
        self.mu = np.mean(x, 0)
        x = x - self.mu
        u, s, v = np.linalg.svd(x)
        self.w = v[:self.k, :]
        return self

    def compress(self, x):
        x = x - self.mu
        z = np.dot(x, self.w.T)
        return z

    def expand(self, z):
        x = np.dot(z, self.w) + self.mu
        return x
