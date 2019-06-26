#! /usr/bin/env python2.7
import cv2, sys, rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


if (len(sys.argv) > 2):
    print(sys.argv)
    print("invalid number of argument")
    sys.exit(1)
else:
    bagFolder = sys.argv[1]

bag = rosbag.Bag(bagFolder + "video.bag")
video = bagFolder + "video.mp4"
bridgeROS2CV = CvBridge()
out = cv2.VideoWriter(video, 0x00000021, 30.0, (640, 480))

for topic, msg, t in bag.read_messages(topics=['/webcam/image_raw']):
    cv_image = bridgeROS2CV.imgmsg_to_cv2(msg, msg.encoding)
    out.write(cv_image)
    #print(msg.header.seq +'KB / '+size+' KB downloaded!', end='\r')
out.release()