# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     naive_bayes_sklearn
   Description :   
   Author :        Yalye
   date：          2018/12/29
-------------------------------------------------
"""

import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# load data
data = pd.read_csv('data/train.csv')
print(data.describe())

data['Age'] = data['Age'].fillna(data['Age'].median())
data['Sex_cleaned'] = np.where(data['Sex'] == 'male', 0, 1)

train_data, test_data = train_test_split(data, test_size=0.5, random_state=int(time.time()))

train_data = train_data[[
    'Survived',
    'Pclass',
    'Sex_cleaned',
    'Age',
    'Fare'
]]

# Train classifier
gnb = GaussianNB()
used_features = [
    'Pclass',
    'Sex_cleaned',
    'Age',
    'Fare'
]

gnb.fit(train_data[used_features].values, train_data['Survived'])

predict_values = gnb.predict(test_data[used_features])

mislabeled_count = (predict_values != test_data['Survived']).sum()
total_test_count = test_data.shape[0]
performance = 1 - (mislabeled_count / total_test_count)
print('The mislabeled count is {} out of total {}, preformance {:05.2f}%'.format(mislabeled_count, total_test_count,
                                                                                 100 * performance))
