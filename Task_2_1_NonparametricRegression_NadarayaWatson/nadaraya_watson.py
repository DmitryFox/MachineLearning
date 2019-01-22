import numpy as np
from math_lib import Kernel, Metric


def nadaraya_watson(value, x, y, h, kernel=Kernel.gaussian, metric=Metric.euclidean):
    size = x.size
    weight = np.zeros(size)
    for i in range(size):
        weight[i] = kernel(metric(value, x[i]) / h)
    return sum(weight * y) / sum(weight)
