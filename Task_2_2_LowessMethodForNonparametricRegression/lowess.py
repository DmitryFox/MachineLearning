import math
import numpy as np
from math_lib import Kernel, Metric


def lowess_method(x, y, iteration, h, kernel=Kernel.gaussian, metric=Metric.euclidean):
    size = x.size
    gamma = np.ones(size)
    result = np.zeros(size)
    for step in range(iteration):
        for t in range(size):
            numerator = 0.
            denominator = 0.
            for i in range(size):
                numerator += y[i] * gamma[i] * kernel(metric(x[i], x[t]) / h)
                denominator += gamma[i] * kernel(metric(x[i], x[t]) / h)
            result[t] = numerator / denominator if denominator != 0. else 0.
        for i in range(size):
            gamma[i] = kernel(math.fabs(result[i] - y[i]))
    return result
