# RadarMapGUI
## File description
### matlab_source folder
* forPython.m: Extract the original Matlab code (from Prof. Chang.), which can see the code about "load high, lon & lat", and use this Matlab code to plot & output binary file (hgt.bin, lon.bin & lat.bin)
* high, lat, lon dat file: It's ASCII data, matlab code will read these data
### Others file
* readBinnay.py: readBinnay.py: Use this code to read binary files & write npy data. It can plot the binary file which can compare with the Matlab plotting result