# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     back_propagation
   Description :   
   Author :        Yalye
   date：          2019/1/2
-------------------------------------------------
"""
import numpy as np


X = np.array(([-2, 4],
    [4, 1],
    [1, 6],
    [2, 4],
    [6, 2]), dtype=float)
y = np.array(([-1],[-1],[1],[1],[1]), dtype=float)

# scale units
X = X/np.amax(X, axis=0)


class Neural_Network():
    def __init__(self, input_size, output_size, hidden_size):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size

        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)

    def forward(self, X):
        self.z = np.dot(X, self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        o = self.sigmoid(self.z3)
        return o

    def sigmoid(self, s):
        return 1/(1 + np.exp(-s))

    def sigmoid_prime(self, s):
        return s * (1 - s)

    def backward(self, X, y, o):
        self.o_error = y - o
        self.o_delta = self.o_error * self.sigmoid_prime(o)

        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.sigmoid_prime(self.z2)

        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.o_delta)

    def train(self, X, y):
        o = self.forward(X)
        self.backward(X, y, o)


NN = Neural_Network(2, 1, 3)
for i in range(10000):
    print("Input: \n" + str(X))
    print("Actual Output: \n" + str(y))
    print("Predicted Output: \n" + str(NN.forward(X)))
    print("Loss: \n" + str(np.mean(np.square(y - NN.forward(X)))))
    print("\n")

    NN.train(X, y)