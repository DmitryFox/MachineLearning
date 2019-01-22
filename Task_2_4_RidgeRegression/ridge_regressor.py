import numpy as np


class RidgeRegression(object):
	def __init__(self):
		self.params = 0

	def fit(self, x, y, alpha=0):
		x = np.hstack((np.ones((x.shape[0], 1)), x))
		g = alpha * np.eye(x.shape[1])
		g[0, 0] = 0
		self.params = np.dot(np.linalg.inv(np.dot(x.T, x) + np.dot(g.T, g)), np.dot(x.T, y))

	def predict(self, x):
		x = np.hstack((np.ones((x.shape[0], 1)), x))
		return np.dot(x, self.params)
