# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     clt
   Description :   
   Author :        Yalye
   date：          2019/1/3
   References:  https://medium.freecodecamp.org/how-to-visualize-the-central-limit-theorem-in-python-b619f5b00168
-------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from wand.image import Image
from wand.display import display

n = 1000

avg = []
for i in range(1, n):
    a = np.random.randint(1, 7, 10)
    avg.append(np.average(a))

def clt(current):
    plt.cla()
    if current == 1000:
        a.event_source.stop()

    plt.hist(avg[0:current])
    plt.gca().set_title('Expected value of die rolls')
    plt.gca().set_xlabel('Average from die roll')
    plt.gca().set_ylabel('Frequency')

    plt.annotate('Die roll = {}'.format(current), [3, 27])

fig = plt.figure()
a = animation.FuncAnimation(fig, clt, interval=1)
