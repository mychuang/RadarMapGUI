# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 13:36:55 2021

@author: Miller
"""

import numpy as np

with open('Data/hgt.bin') as f:
    rectype = np.dtype(np.float64)
    bdata = np.fromfile(f, dtype=rectype)
hgt = np.reshape(bdata, (1006, 1913))

with open('Data/lon.bin') as f:
    rectype = np.dtype(np.float64)
    bdata = np.fromfile(f, dtype=rectype)
lon = np.reshape(bdata, (1006, 1913))

with open('Data/lat.bin') as f:
    rectype = np.dtype(np.float64)
    bdata = np.fromfile(f, dtype=rectype)
lat = np.reshape(bdata, (1006, 1913))

#%%
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,16)) #create figure
ax = fig.add_subplot(1, 1, 1) #create ax within figure
ax.contour(lon, lat, hgt, 8, cmap='jet')
   
ax.xaxis.set_tick_params(rotation=30, labelsize=16) #setting xticks
ax.minorticks_on()
ax.yaxis.set_tick_params(labelsize=16) #setting yticks
ax.minorticks_on()

ax.set_title('Hight contour',fontsize=20)

#%%
np.save('hgt', hgt)
np.save('lon', lon)
np.save('lat', lat)

