# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tf_decision_tree
   Description :   
   Author :        Yalye
   date：          2018/12/21
-------------------------------------------------
"""


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from pprint import pprint

# step 1: load data
data_path = "./data/"
names = ('animal_name', 'hair', 'feathers', 'eggs', 'milk',
         'airbone', 'aquatic', 'predator', 'toothed', 'backbone',
         'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'class',)
formats = ('S1',) + (('i4',) * 17)
zoo_data = np.loadtxt(data_path + 'zoo.data', delimiter=',', dtype={'names': names,
                                                                    'formats': formats}, skiprows=0)
zoo_data_df = pd.DataFrame(zoo_data)
zoo_data_df = zoo_data_df.drop('animal_name', axis=1)
sample_number = zoo_data.shape[0]
print(sample_number)
print(zoo_data_df)

train_features = zoo_data_df.iloc[:80,:-1]
test_features = zoo_data_df.iloc[80:,:-1]
train_targets = zoo_data_df.iloc[:80,-1]
test_targets = zoo_data_df.iloc[80:,-1]

tree = DecisionTreeClassifier(criterion = 'entropy').fit(train_features,train_targets)

prediction = tree.predict(test_features)

print("The prediction accuracy is: ", tree.score(test_features,test_targets)*100,"%")
