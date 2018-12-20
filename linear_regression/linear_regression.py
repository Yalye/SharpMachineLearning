# -*- coding: utf-8 -*-

import pandas as pd
import statsmodels.formula.api as smf
from mpl_toolkits.mplot3d import Axes3D

"""
-------------------------------------------------
   File Name：     linear_regression
   Description :
   Author :        Yalye
   date：          2018/11/11
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np
import os

data_path = "./data/"
house_data = np.loadtxt(data_path + 'house_prices.csv', delimiter=',', dtype=float, skiprows=0)

sample_number = house_data.shape[0]

X = house_data[:, :2]
y = house_data[:, 2]

print('First 10 samples of the dataset: ')
print(house_data[0:10, :])

# feature normalization, using zscore normalization
from scipy import stats
X_norm = stats.zscore(X)
X_norm = np.append(np.ones((sample_number, 1)), X_norm, axis=1)

print('First 10 samples of the norm dataset: ')
print(X_norm[:10])

# linear regression
alpha = 0.01
num_iters = 400

theta = np.ndarray.flatten(np.zeros((3, 1)))
J_history = np.zeros((num_iters, 1))

for i in range(num_iters):
    theta = theta - np.dot(np.transpose(X_norm), np.ndarray.flatten(np.dot(X_norm, theta)) - y) * (
        alpha / sample_number)
    J_cost = 0
    for j in range(sample_number):
        J_cost = J_cost + (
            (1 / (2 * sample_number)) * np.square(np.dot(np.transpose(theta), np.transpose(X_norm[j, :])) - y[j]))
    J_history[i] = J_cost

print('theta is ',theta)
plt.plot(J_history)
plt.show()

# predict house price
test_square = 1600
test_bed_room = 3
predict_values = ([1,
                   (test_square - np.mean(X[:, 0])) / (np.std(X[:, 0])),
                   (test_bed_room - np.mean(X[:, 1])) / np.std(X[:, 1])])
print(predict_values)
predict_selling_price = np.dot(predict_values, theta)
print('The price of house with area of {0} and bedrooms of {1} is {2}'.format(test_square, test_bed_room, predict_selling_price))
