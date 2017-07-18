# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:22:59 2017

@author: sunshine
"""
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:34:41 2017

@author: sunshine
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage import io,data
import numpy as np
import matplotlib.pyplot as plt

# Data to be represented
#X = np.linspace(0,500,20)
#M = (1+np.sin(X/20)+np.random.uniform(0.75,1.0,X.size)) * np.linspace(1,0.2,X.size)
#W = (1+np.sin(X/20)+np.random.uniform(0.75,1.0,X.size)) * np.linspace(1,0.2,X.size)
X=np.array([20,40,60,80,100])
apl=np.array([6.847,6.418,6.205,5.862,5.841])
node=np.array([263,292,325,357,364])
link=np.array([465,612,732,884,910])
rongliang=np.array([529600,1550400,3455200,5706400,6323200])


fig = plt.figure(figsize=(6,6), dpi=500,facecolor="white")
axes = plt.subplot(111, axisbelow=True)

plt.bar(X+8, -link, width=8, facecolor='#5A5AAD', edgecolor='white')
for i,x in enumerate(X):
    x+=0.3
    y = -link[i]-15
    plt.text(x+8,y, -y, color='#484891', size=12,
             horizontalalignment='center',  verticalalignment='top')

plt.bar(X, -node, width=8, facecolor='#AD5A5A', edgecolor='white')
for i,x in enumerate(X):
    x+=0.3
    y = -node[i] - 15
    plt.text(x,y,-y, color='#743A3A', size=12,
             horizontalalignment='center',  verticalalignment='top')
plt.bar(X+4, rongliang/5000, width=16, facecolor='#408080', edgecolor='white')

#axes.set_xlim([2000,2100])
axes.set_ylim([-1000,1500])
axes.set_xticks([])
axes.set_yticks([-1000,-500,0,400,800,1200])
axes.set_yticklabels([1000,500,0,200,400,600])


axes.spines['top'].set_color('none')
axes.spines['left'].set_color('none')
axes.spines['right'].set_color('none')
axes.spines['bottom'].set_color('none')
axes.yaxis.set_ticks_position('right')


plt.text(12,1300,"2013-2017", color='black', size=30,
         horizontalalignment='left', verticalalignment='bottom')
plt.text(12,1200,"The Resource Situation in China Mobile\n Optical Backbone Network", color='.55', size=8,
         horizontalalignment='left', verticalalignment='top')
plt.text(5,1100,"Resources(10^3 G)",rotation=90,color='#5A5AAD',size=13)
plt.text(5,-200,"Nodes and Links",rotation=90,color='#AD5A5A',size=13)
print plt.style.available 
plt.savefig('E:/PY/test.png',dpi=600)
plt.show()