import numpy as np


def cal_euclidean(a, b):
    return np.sqrt(np.sum(np.square(a - b)))


def cal_manhattan(a, b):
    return np.sum(np.abs(a - b))


def cal_cosine(a, b):
    d = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return d / (norm_a * norm_b)


a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))
