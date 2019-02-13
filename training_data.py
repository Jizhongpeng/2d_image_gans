import numpy as np
import math


def get_y(x):
    return np.sin(x)   # a line

def sample_data(n=3000, scale=2*np.pi): # set scale = 1
    data = []

    x = scale*(np.random.random_sample((n,))-0.5)

    for i in range(n):
        yi = get_y(x[i])
        data.append([x[i], yi])

    return np.array(data)
