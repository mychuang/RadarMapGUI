import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

RadarName = dict()
RadarName['RCCG'] = [120.4609,22.67358,19.9693]


class Radar_fc:
    def __init__(self):
        self.lat = sio.loadmat('../Data/lat.mat')['lat']
        self.lon = sio.loadmat('../Data/lon.mat')['lon']
        self.hgt = sio.loadmat('../Data/hgt.mat')['high']
        self.Select_Radar = []


    def ppi_blocking(self):
        range_Max = 500

        block = np.zeros((361,range_Max))
        blockh = np.copy(block)
        blockh_rz = np.copy(block)
        xxx = np.copy(block)
        yyy = np.copy(block)

        aearth = 6371.22
        [rd_lon, rd_lat, rd_hgt]=RadarName['RCCG']


        for Az in range(361):
            i = (450 - Az) / 360 * 2 * np.pi
            minelv = 0;
            for RG in range(range_Max):
                xxx[Az,RG] = (RG*np.cos(i)) * 180 / np.pi / np.cos( ((RG*np.sin(i)) /aearth*180/np.pi + rd_lat) *np.pi /360 ) / aearth + rd_lon
                yyy[Az,RG] = (RG*np.sin(i)) /aearth*180/np.pi + rd_lat
                xx = ((RG * np.cos(i)) * 180 / np.pi / np.cos(((RG * np.sin(i)) / aearth * 180 / np.pi + rd_lat) * np.pi / 360) /
                      aearth + rd_lon - self.lon[0, 0]) / (self.lon[0, -1] - self.lon[0, 0]) * np.shape(self.lon)[1]
                yy = ((RG * np.sin(i)) / aearth * 180 / np.pi + rd_lat - self.lat[0, 0]) / (
                            self.lat[-1, 0] - self.lat[0, 0]) * np.shape(self.lat)[0]
                ix1 = int(np.fix(xx)) - 1
                ix2 = ix1 + 1
                iy1 = int(np.fix(yy)) - 1
                iy2 = iy1 + 1

                if ix1 <= 0 or ix2 >= np.shape(self.lon)[0] + 1 or iy1 <= 0 or iy2 >= np.shape(self.lon)[1] + 1:
                    rz = 0
                else:
                    if ix2 >= int(np.shape(self.hgt)[1]) or iy2 >= int(np.shape(self.hgt)[0]):
                        rz = 0
                    else:
                        rz = ((ix2 - xx + 1) * self.hgt[iy1, ix1] + (xx - ix1 - 1) * self.hgt[iy1, ix2]) * (
                                    iy2 - yy + 1) + (yy - iy1 - 1) * \
                             ((ix2 - xx + 1) * self.hgt[iy2, ix1] + (xx - ix1 - 1) * self.hgt[iy2, ix2])
                    if rz < -999:
                        rz = 0
                for elv in np.arange(minelv, 15+0.5, 0.5):
                    h = (aearth * (1.0 + (RG/aearth)**2 + 2.0*RG/aearth*np.sin(elv*np.pi/180))**(0.5) - aearth)* 1000 + rd_hgt
                    if rz <=h:
                        block[Az,RG] = elv
                        blockh[Az,RG] = h
                        blockh_rz[Az,RG] = h-rz
                        minelv = elv
                        break
        ppi_blocking = (xxx,yyy,block,blockh,blockh_rz)

        return(ppi_blocking)









    def Plt(self):
        plt.pcolormesh(self.lon,self.lat,self.hgt)
        plt.colorbar()
        plt.show()