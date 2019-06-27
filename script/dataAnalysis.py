#! /usr/bin/env python2.7
import sys, csv, os
import numpy as np
import matplotlib.pyplot as plt

if (len(sys.argv) == 2):
    csvFolder = sys.argv[1]
    printing = False
if (len(sys.argv) == 3):
    csvFolder = sys.argv[1]
    printing = sys.argv[2]
elif (len(sys.argv) > 3):
    print(sys.argv)
    print("invalid number of argument")
    sys.exit(1)


csvImuPath = csvFolder + "imu.csv"
csvGesturesPath = csvFolder + "gestures.csv"


gesturesName = []
with open(csvGesturesPath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        gesturesName.append(row[2])
    gesturesName = gesturesName[1:]

imuData = np.genfromtxt(csvImuPath, delimiter=',')
imuData = imuData[1:,:]
gestures = np.genfromtxt(csvGesturesPath, delimiter=',')
gestures = np.vstack([gestures[1:,:], gestures[-1, :]])
gestures[-1,0] = gestures[-1,0] + 5 


timeImu = imuData[:,0] + imuData[:,1]/10**9
timeGestures = gestures[:,0] + gestures[:,1]/10**9

gesturesIndex = []
for time in timeGestures:
    gesturesIndex.append(abs(timeImu - time).argmin())

module_vel = np.sqrt(np.sum(np.power(imuData[:,3:6],2), axis=1))
labelings = []

for i in range(0,len(gestures)-1):
    g1 = module_vel[gesturesIndex[i]:gesturesIndex[i+1]+1]
    SUMM = np.sum(g1)
    weightedAverage = np.sum(g1*timeImu[gesturesIndex[i]:gesturesIndex[i+1]+1])/np.sum(g1)
    waIndex = abs(timeImu - weightedAverage).argmin()
    c = 1
    while True:
        summ = np.sum(module_vel[waIndex-c:waIndex+c+1])
        if summ > 0.95*SUMM:
            break
        c = c + 1
    start = waIndex-c
    if start < gesturesIndex[i]:
        start = gesturesIndex[i]
    end = waIndex+c+1
    if end > gesturesIndex[i+1]+1:
        end = gesturesIndex[i+1]+1
    labelings.append([start, end])


csvName = csvFolder + 'imu_labeled.csv'
if not(os.path.isfile(csvName)):
        with open(csvName, 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter = ',')
            values = ['ros_seconds', 'ros_nanoseconds', 'android_millis', 'angular_vel_x', 'angular_vel_y', 'angular_vel_z', 'linear_acc_x', 'linear_acc_y', 'linear_acc_z', 'gesture']
            filewriter.writerow(values)
            gestureTag = 0

            for index in range(0, len(imuData)):
                values = imuData[index].tolist()
                l = labelings[gestureTag]
                if index < l[0]:
                    values.append("nan")
                elif index >= l[0] and index <= l[1]:
                    values.append(gesturesName[gestureTag])
                elif index > l[1]:
                    values.append("nan")
                    gestureTag = gestureTag + 1
                filewriter.writerow(values)
else:
    print("Warning the file already exist")

if printing:
    plt.figure(1)
    plt.subplot(6, 1, 1)
    plt.scatter(timeImu[gesturesIndex], imuData[gesturesIndex,6], c='yellow', s=50)
    plt.plot(timeImu, imuData[:,6])
    for l in labelings:
        plt.scatter(timeImu[l[0]], imuData[l[0],6], c='red', s=50)
        plt.scatter(timeImu[l[1]], imuData[l[1],6], c='red', s=50)

    plt.subplot(6, 1, 2)
    plt.scatter(timeImu[gesturesIndex], imuData[gesturesIndex,7], c='yellow', s=50)
    plt.plot(timeImu, imuData[:,7])
    for l in labelings:
        plt.scatter(timeImu[l[0]], imuData[l[0],7], c='red', s=50)
        plt.scatter(timeImu[l[1]], imuData[l[1],7], c='red', s=50)

    plt.subplot(6, 1, 3)
    plt.scatter(timeImu[gesturesIndex], imuData[gesturesIndex,8], c='yellow', s=50)
    plt.plot(timeImu, imuData[:,8])
    for l in labelings:
        plt.scatter(timeImu[l[0]], imuData[l[0],8], c='red', s=50)
        plt.scatter(timeImu[l[1]], imuData[l[1],8], c='red', s=50)

    plt.subplot(6, 1, 4)
    plt.scatter(timeImu[gesturesIndex], imuData[gesturesIndex,3], c='yellow', s=50)
    plt.plot(timeImu, imuData[:,3])
    for l in labelings:
        plt.scatter(timeImu[l[0]], imuData[l[0],3], c='red', s=50)
        plt.scatter(timeImu[l[1]], imuData[l[1],3], c='red', s=50)

    plt.subplot(6, 1, 5)
    plt.scatter(timeImu[gesturesIndex], imuData[gesturesIndex,4], c='yellow', s=50)
    plt.plot(timeImu, imuData[:,4])
    for l in labelings:
        plt.scatter(timeImu[l[0]], imuData[l[0],4], c='red', s=50)
        plt.scatter(timeImu[l[1]], imuData[l[1],4], c='red', s=50)

    plt.subplot(6, 1, 6)
    plt.scatter(timeImu[gesturesIndex], imuData[gesturesIndex,5], c='yellow', s=50)
    plt.plot(timeImu, imuData[:,5])
    for l in labelings:
        plt.scatter(timeImu[l[0]], imuData[l[0],5], c='red', s=50)
        plt.scatter(timeImu[l[1]], imuData[l[1],5], c='red', s=50)

    plt.show()