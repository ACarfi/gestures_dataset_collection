#! /usr/bin/env python2.7
import sys
import numpy as np
import matplotlib.pyplot as plt

if (len(sys.argv) > 2):
    print(sys.argv)
    print("invalid number of argument")
    sys.exit(1)
else:
    csvFolder = sys.argv[1]

csvImuPath = csvFolder + "imu.csv"
csvGesturesPath = csvFolder + "gestures.csv"

imuData = np.genfromtxt(csvImuPath, delimiter=',')
gestures = np.genfromtxt(csvGesturesPath, delimiter=',')
timeImu = imuData[2:-1,0] + imuData[2:-1,1]/10**9
timeGestures = gestures[2:-1,0] + gestures[2:-1,1]/10**9
print len(timeGestures)
plt.scatter(timeGestures, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
plt.plot(timeImu, imuData[2:-1,-1])
plt.show()
