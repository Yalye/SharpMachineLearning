# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     normalization
   Description :   
   Author :        Tingur
   date：          2018/12/15
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import pandas as pd

data_path = "./data/"
results = pd.read_excel(data_path + 'house_prices.xls', usecols=[0,1])
print(results.columns.values)

# zscore normalization
from scipy import stats
df_std = stats.zscore(results)

# min max normalization
df_minmax = (results - results.min()) / (results.max() - results.min())
df_minmax = df_minmax.as_matrix()
print(df_minmax)
# from sklearn import preprocessing
# minmax_scale = preprocessing.MinMaxScaler().fit(results[['Area', 'Bedrooms']])
# df_minmax = minmax_scale.transform(results[['Area', 'Bedrooms']])

plt.figure(1, figsize=(8, 6))
plt.scatter(results['Bedrooms'], results['Area'], color='green', label='input scale', alpha=0.5)
plt.title('Area and Bedrooms of the house dataset')
plt.xlabel('Bedrooms')
plt.ylabel('Area')
plt.legend(loc='upper left')
plt.grid()
plt.tight_layout()

plt.figure(2, figsize=(8, 6))
plt.scatter(df_std[:,1], df_std[:,0], color='red', label='standardized', alpha=0.3)
plt.scatter(df_minmax[:,1], df_minmax[:,0], color='blue', label='min max normalization', alpha=0.3)
plt.show()


#
#
#
# X_mean = np.mean(X, axis=0)
# X_std = np.std(X, axis=0)
#
# from scipy import stats
# p = stats.zscore(X)
#
# X_norm = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
# X_norm = np.append(np.ones((sample_number, 1)), X_norm, axis=1)
# print('First 10 samples of the norm dataset: ')