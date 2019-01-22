import math
import numpy as np


class Kernel:
    @staticmethod
    def rectangular(u):
        return 1. / 2. if math.fabs(u) <= 1. else 0.

    @staticmethod
    def triangular(u):
        return 1. - math.fabs(u) if math.fabs(u) <= 1. else 0.

    @staticmethod
    def epanechnikov(u):
        return 3. / 4. * (1. - math.pow(u, 2.)) if math.fabs(u) <= 1. else 0.

    @staticmethod
    def quartic(u):
        return 15. / 16. * math.pow(1. - math.pow(u, 2.), 2.) if math.fabs(u) <= 1. else 0.

    @staticmethod
    def triweight(u):
        return 35. / 32. * math.pow(1. - math.pow(u, 2.), 3.) if math.fabs(u) <= 1. else 0.

    @staticmethod
    def gaussian(u):
        return 1. / math.sqrt(2. * math.pi) * math.exp(-1. / 2. * math.pow(u, 2.))


class Metric:
    @staticmethod
    def euclidean(p, q):
        return math.sqrt(math.pow(p - q, 2.))


def sse(y_original, y_result):
    return np.sum(pow(y_original - y_result, 2))
