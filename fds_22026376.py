# -*- coding: utf-8 -*-
"""
Created on Tue May  2 22:57:05 2023

@author: shanm
"""
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Reading the csv filr into array
data_array = np.genfromtxt('data6.csv', delimiter=',')
print(data_array)

histo, bin_edges = np.histogram(data_array, bins=20, range=(2.0,4.5))
# plt.hist(data_array, bins=30,range=(2.0,4.5))
#calculate the bincentre location and binwidth
xdst = 0.5* (bin_edges[1:] + bin_edges[: -1])
wdst = bin_edges[1:] - bin_edges[: -1]

#normalise the distribution
ydst = histo/np.sum(histo)

#cumulative ditribution
cdst = np.cumsum(ydst)

plt.figure(dpi=600)
#find the mean value
xmean = np.sum(xdst*ydst)
plt.plot([xmean,xmean],[0.0, max(ydst)], c='red')

plt.text(x=xmean-1.35 , y=0.08, s=f"Mean weight : {xmean}", fontsize=12, c='black')
plt.bar(xdst ,ydst , width=0.9*wdst, color="green", label="10% of newborns are born with a weight above X%")

#to find the value of 10% of newborn distribution  above X value
indx = np.argmin(np.abs(cdst - 0.90))
xabove = bin_edges[indx]

plt.bar(xdst[0:indx],ydst[0:indx], width=0.9*wdst[0:indx], color='royalblue', label="Distribution weight of newborn babies")
plt.plot([xabove,xabove],[0.0, max(ydst)], 'k', c='black')
plt.text(x=xmean + 0.40, y=max(ydst), s=f"X value {xabove}", fontsize=12, c='black')

plt.xlabel('Newborn Weight (kg)')
plt.ylabel('Probability')
plt.title('Distribution of weight of newborn babies')
plt.legend(bbox_to_anchor = (1.01, 0.99), fontsize = 10)
plt.show()