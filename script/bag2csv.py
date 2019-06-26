#! /usr/bin/env python3.5
import rosbag, os, rospkg, csv, sys
from std_msgs.msg import Header, String
from sensor_msgs.msg import Imu

if (len(sys.argv) > 2):
    print(sys.argv)
    print("invalid number of argument")
    sys.exit(1)
else:
    bagFolder = sys.argv[1]

filesName = ['imu', 'info', 'gestures']

for fileName in filesName:
    bag = rosbag.Bag(bagFolder + "/" + fileName + ".bag")
    csvName = bagFolder + "/" + fileName + ".csv"
    if not(os.path.isfile(csvName)):
        with open(csvName, 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter = ',')
            firstIteration = True
            if fileName != 'info':
                for topic, msg, t in bag.read_messages():
                    values = []
                    if fileName == 'imu':   
                        if firstIteration:
                            header = ['ros_seconds', 'ros_nanoseconds', 'android_millis', 'angular_vel_x', 'angular_vel_y', 'angular_vel_z', 'linear_acc_x', 'linear_acc_y', 'linear_acc_z']
                            filewriter.writerow(header)       
                            firstIteration = False      
                        values.append(msg.header.stamp.secs)
                        values.append(msg.header.stamp.nsecs)
                        values.append(int(msg.header.frame_id))
                        values.append(msg.angular_velocity.x)
                        values.append(msg.angular_velocity.y)
                        values.append(msg.angular_velocity.z)
                        values.append(msg.linear_acceleration.x)
                        values.append(msg.linear_acceleration.y)
                        values.append(msg.linear_acceleration.z)
                    elif fileName == 'gestures':
                        if firstIteration:
                            header = ['ros_seconds', 'ros_nanoseconds', 'gesture_name']
                            filewriter.writerow(header)       
                            firstIteration = False   
                        values.append(msg.stamp.secs)
                        values.append(msg.stamp.nsecs)
                        values.append(msg.frame_id)
                    filewriter.writerow(values)
            else:
                for topic, msg, t in bag.read_messages(topics =['/name']):
                    values = ['name']
                    values.append(msg.frame_id)
                    filewriter.writerow(values)
                for topic, msg, t in bag.read_messages(topics =['/surname']):
                    values = ['surname']
                    values.append(msg.frame_id)
                    filewriter.writerow(values)
                for topic, msg, t in bag.read_messages(topics =['/age']):
                    values = ['age']
                    values.append(msg.frame_id)
                    filewriter.writerow(values)
                for topic, msg, t in bag.read_messages(topics =['/gender']):
                    values = ['gender']
                    values.append(msg.frame_id)
                    filewriter.writerow(values)
                for topic, msg, t in bag.read_messages(topics =['/email']):
                    values = ['email']
                    values.append(msg.frame_id)       
                    filewriter.writerow(values)     
                for topic, msg, t in bag.read_messages(topics =['/language']):
                    values = ['language']
                    values.append(msg.frame_id)      
                    filewriter.writerow(values)      
    bag.close()