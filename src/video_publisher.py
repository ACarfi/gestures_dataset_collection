#! /usr/bin/env python3.5
import cv_bridge, rospy
from lib.Tools.camera import Camera
from sensor_msgs.msg import Image



if __name__ == '__main__':
    rospy.init_node('video_publisher', disable_signals=True)
    camera = Camera(0)
    camera.initialize()
    self.image_pub = rospy.Publisher("/video",Image)
    r = rospy.Rate(30)
    while True:
        try:
            frame = self.camera.get_frame()
            r.sleep()
        except KeyboardInterrupt:
            break