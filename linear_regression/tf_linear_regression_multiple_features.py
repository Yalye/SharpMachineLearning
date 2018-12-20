# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tf_linear_regression
   Description :   use linear regression to calculate the relationship between the number of fires and thefts in a neighborhood.
   Author :        Yalye
   date：          2018/10/21
-------------------------------------------------
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

learning_reate = 0.001
training_epochs = 10000
display_step = 50

# Step 1: read data
data_path = "./data/"
house_data = np.loadtxt(data_path + 'house_prices.csv', delimiter=',', dtype=float, skiprows=0)
sample_count = house_data.shape[0]
feature_count = 2

train_X = house_data[:, :2]
from scipy import stats
train_X_norm = stats.zscore(train_X)
train_Y = house_data[:, 2:]

# Step 2: create placeholders for input X (bedrooms and area) and label Y (prices)
X = tf.placeholder(tf.float32, [sample_count,feature_count])
Y = tf.placeholder(tf.float32, [sample_count,1])

# Step 3: create weight and bias, initialized to 0
W = tf.Variable(tf.zeros([feature_count,1]), dtype=np.float32, name='weights')
b = tf.Variable(tf.zeros([1]), dtype=np.float32, name='bias')

# Step 4: construct model to predict Y (number of theft) from the number of fire
Y_predicted = tf.add(tf.matmul(X, W), b)

# Step 5: use the square error as the loss function
# loss = tf.square(Y - Y_predicted, name='loss')
loss = tf.reduce_sum(tf.square(Y_predicted - Y)) / (2 * sample_count)

# Step 6: use gradient descent to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_reate).minimize(loss)
with tf.Session() as sess:
    # Step 7: initialize all the variables, in this case, w and b
    sess.run(tf.initialize_all_variables())

    J_history = np.zeros((training_epochs, 1))
    # Step 8: train the model
    for i in range(training_epochs):
        sess.run(optimizer, feed_dict={X: np.asarray(train_X_norm), Y: np.asarray(train_Y)})

        cost = sess.run(loss, feed_dict={X: np.asarray(train_X_norm),Y: np.asarray(train_Y)})
        J_history[i] = cost
        # Display logs per epoch step
        if (i + 1) % display_step == 0:
            print("Step:", "%04d" % (i + 1), "Cost=", "{:.2f}".format(cost,  "W=", sess.run(W), "b=", sess.run(b)))

    plt.plot(J_history)
    plt.show()

    # Optimization finish
    training_loss = sess.run(loss, feed_dict={X: train_X_norm, Y: train_Y})
    print('training loss=', training_loss, 'w=', sess.run(W), 'b=', sess.run(b))

    w_value = sess.run(W)
    b_value = sess.run(b)

    test_square = 1600
    test_bed_room = 3
    predict_input = ([(test_square - np.mean(train_X[:, 0])) / (np.std(train_X[:, 0])),
                       (test_bed_room - np.mean(train_X[:, 1])) / np.std(train_X[:, 1])])

    nd = np.asarray(predict_input).reshape((1,2))
    wd = sess.run(W).astype(np.float64)
    mul = tf.matmul(nd, wd)

    predict_price = tf.add(mul, sess.run(b))
    print(sess.run(predict_price))
    # Graphic display

# theta is  [330950.55907296  99953.04536259   3763.7699476 ]
# [1, -0.4802550853113349, -0.2260933675776883]
# The price of house with area of 1600 and bedrooms of 3 is 282096.6373229863