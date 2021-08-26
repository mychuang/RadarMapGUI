import numpy as np
import matplotlib.pyplot as plt
class Radar_fc:
    def __init__(self):
        self.lat = np.load('../Data/lat.npy')
        self.lon = np.load('../Data/lon.npy')
        self.hgt = np.load('../Data/hgt.npy')

    def Plt(self):
        plt.pcolormesh(self.lon,self.lat,self.hgt)
        plt.colorbar()
        plt.show()