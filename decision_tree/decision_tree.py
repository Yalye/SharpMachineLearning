# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     decision_tree.py
   Description :   
   Author :        Yalye
   date：          2018/12/19
-------------------------------------------------
"""

import pandas as pd
import numpy as np
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


def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = np.sum(
        [(-counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts)) for i in range(len(elements))])
    return entropy

def info_gain(data, split_attribute_name, target_name='class'):
    total_entropy = entropy(data[target_name])

    vals,counts = np.unique(data[split_attribute_name],return_counts=True)

    weighted_entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) for i in range(len(vals))])

    information_gain = total_entropy - weighted_entropy

    return information_gain


def ID3(data, original_data, features, target_attribute_name='class', parent_node_class=None):
    # if all target_values have the same value, return this value
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    elif len(data) == 0:
        return np.unique(original_data[target_attribute_name])[
            np.argmax(np.unique(original_data[target_attribute_name], return_counts=True)[1])]
    elif len(features) == 0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_attribute_name])[
            np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]

        item_values = [info_gain(data,feature,target_attribute_name) for feature in features]

        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]

        tree = {best_feature: {}}

        for value in np.unique(data[best_feature]):
            value = value
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = ID3(sub_data, data, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree

        return (tree)

def predict(query,tree,default = 1):
    attribute = list(tree.keys())[0]
    if query[attribute] in tree[attribute].keys():
        try:
            result = tree[attribute][query[attribute]]
            if isinstance(result, dict):
                return predict(query, result)
            else:
                return result
        except:
            return default


def train_test_split(dataset):
    training_data = dataset.iloc[:80].reset_index(drop=True)
    testing_data = dataset.iloc[80:].reset_index(drop=True)
    return training_data, testing_data

def test(data, tree):
    queries = data.iloc[:, :-1].to_dict(orient='records')
    predicted = pd.DataFrame(columns=['predicted'])
    for i in range(len(data)):
        predicted.loc[i,'predicted'] = predict(queries[i], tree, 1.0)
    print('The prediction accuracy is: ', (np.sum(predicted['predicted']== data["class"])/len(data))*100,'%')

training_data=train_test_split(zoo_data_df)[0]
testing_data=train_test_split(zoo_data_df)[1]
tree = ID3(training_data,training_data,training_data.columns[:-1])
pprint(tree)
test(testing_data,tree)
