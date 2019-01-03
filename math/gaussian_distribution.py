# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     gaussian_distribution
   Description :   
   Author :        Yalye
   date：          2019/1/3
-------------------------------------------------
"""

import matplotlib.pyplot as plt, matplotlib.mlab as mlab
import numpy as np
import math

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, mlab.normpdf(x, mu, sigma))
plt.show()