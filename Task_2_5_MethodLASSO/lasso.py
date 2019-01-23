import numpy as np
from copy import deepcopy


class Lasso:
	def __init__(self, alpha=1.0, max_iteration=1000, fit_intercept=True):
		self.alpha = alpha
		self.max_iter = max_iteration
		self.fit_intercept = fit_intercept
		self.coefficient = None
		self.intercept_ = None

	def _soft_thresholding_operator(self, x, lambda_):
		if x > 0 and lambda_ < abs(x):
			return x - lambda_
		elif x < 0 and lambda_ < abs(x):
			return x + lambda_
		else:
			return 0

	def fit(self, X, y):
		if self.fit_intercept:
			X = np.column_stack((np.ones(len(X)), X))

		beta = np.zeros(X.shape[1])
		if self.fit_intercept:
			beta[0] = np.sum(y - np.dot(X[:, 1:], beta[1:])) / (X.shape[0])

		for iteration in range(self.max_iter):
			start = 1 if self.fit_intercept else 0
			for j in range(start, len(beta)):
				tmp_beta = deepcopy(beta)
				tmp_beta[j] = 0.0
				r_j = y - np.dot(X, tmp_beta)
				arg1 = np.dot(X[:, j], r_j)
				arg2 = self.alpha * X.shape[0]

				beta[j] = self._soft_thresholding_operator(arg1, arg2) / (X[:, j] ** 2).sum()

				if self.fit_intercept:
					beta[0] = np.sum(y - np.dot(X[:, 1:], beta[1:])) / (X.shape[0])

		if self.fit_intercept:
			self.intercept_ = beta[0]
			self.coefficient = beta[1:]
		else:
			self.coefficient = beta

		return self

	def predict(self, X):
		y = np.dot(X, self.coefficient)
		if self.fit_intercept:
			y += self.intercept_ * np.ones(len(y))
		return y
