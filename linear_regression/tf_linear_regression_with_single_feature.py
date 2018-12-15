# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tf_linear_regression
   Description :   use linear regression to calculate the relationship between the number of fires and thefts in a neighborhood.
   Author :        Tingur
   date：          2018/10/21
-------------------------------------------------
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import xlrd

learning_reate = 0.001
training_epochs = 100
display_step = 50

# Step 1: read data
book = xlrd.open_workbook('data/fires_thefts.xls', encoding_override='utf-8')
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
print(data)
n_samples = sheet.nrows - 1

# Step 2: create placeholders for input X (number of fire) and label Y (number of theft)
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')

# Step 3: create weight and bias, initialized to 0
w = tf.Variable(0.0, name='weights')
b = tf.Variable(0.0, name='bias')

# Step 4: construct model to predict Y (number of theft) from the number of fire
Y_predicted = X * w + b

# Step 5: use the square error as the loss function
loss = tf.square(Y - Y_predicted, name='loss')

# Step 6: use gradient descent to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_reate).minimize(loss)

with tf.Session() as sess:
    # Step 7: initialize all the variables, in this case, w and b
    sess.run(tf.initialize_all_variables())

    train_X, train_Y = data.T
    # Step 8: train the model
    for i in range(training_epochs):
        for x, y in data:
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (i + 1) % display_step == 0:
            c = sess.run(loss, feed_dict={X: train_X, Y: train_Y})
            print(c)
            # print('Epoch:', '%04d' % (i+1), 'cost=', '{:.9f}'.format(c), \
            #     "w=", sess.run(w), 'b=', sess.run(b))

    # Optimization finish
    training_loss = sess.run(loss, feed_dict={X: train_X, Y: train_Y})
    print('training loss=', training_loss, 'w=', sess.run(w), 'b=', sess.run(b))

    # Graphic display
    plt.plot(train_X, train_Y, 'ro', label='original data')
    plt.plot(train_X, sess.run(w) * train_X + sess.run(b), label='fitted line')
    plt.legend()
    plt.show()
