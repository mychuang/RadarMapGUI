from Radar_fc import Radar_fc as RD
import matplotlib.pyplot as plt

RADAR = RD()
ppi_blocking=RADAR.ppi_blocking()
(xxx,yyy,block,blockh,blockh_rz)=ppi_blocking
plt.pcolormesh(xxx,yyy,block)
plt.show()


