# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:34:41 2017

@author: sunshine
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
#X = np.linspace(0,500,20)
#M = (1+np.sin(X/20)+np.random.uniform(0.75,1.0,X.size)) * np.linspace(1,0.2,X.size)
#W = (1+np.sin(X/20)+np.random.uniform(0.75,1.0,X.size)) * np.linspace(1,0.2,X.size)
X=np.array([20,40,60,80,100])
apl=np.array([6.847,6.418,6.205,5.862,5.841])
node=np.array([263,292,325,357,364])
link=np.array([465,612,732,884,910])


fig = plt.figure(figsize=(6,6), dpi=72,facecolor="white")
axes = plt.subplot(111, axisbelow=True)

plt.bar(X, +link, width=12, facecolor='#5A5AAD', edgecolor='white')
for i,x in enumerate(X):
    x+=0.3
    y = link[i] + 10
    plt.text(x,y, y, color='#484891', size=12,
             horizontalalignment='center',  verticalalignment='bottom')

plt.bar(X, -node, width=12, facecolor='#AD5A5A', edgecolor='white')
for i,x in enumerate(X):
    x+=0.3
    y = -node[i] - 15
    plt.text(x,y,-y, color='#743A3A', size=12,
             horizontalalignment='center',  verticalalignment='top')

#axes.set_xlim([2000,2100])
axes.set_ylim([-500,1300])
axes.set_xticks([])
axes.set_yticks([+300,-20])
axes.set_yticklabels(['LINKS', 'NODES'])
labels = axes.get_yticklabels()
labels[0].set_rotation(90)
labels[0].set_size(13)
#labels[0].set_bold(True)
labels[0].set_color('#5A5AAD')
labels[1].set_rotation(90)
labels[1].set_size(13)
labels[1].set_color('#AD5A5A')

axes.spines['top'].set_color('none')
axes.spines['left'].set_color('none')
axes.spines['right'].set_color('none')
axes.spines['bottom'].set_color('none')
axes.yaxis.set_ticks_position('left')


plt.text(5,1100,"2013-17", color='black', size=30,
         horizontalalignment='left', verticalalignment='bottom')
plt.text(5,1000,"The number of nodes and links in China Mobile\n Optical Bcakbone Network", color='.55', size=8,
         horizontalalignment='left', verticalalignment='top')


plt.savefig('E:/PY/test.png')
plt.show()