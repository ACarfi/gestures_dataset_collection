import rospy
from sensor_msgs.msg import Image


class CameraMonitor():
    def __init__(self, topic):
        self.topic = topic
        self.published = False
        self.calibrated = False
        self.message = Image()

        rospy.Subscriber(topic, Image, self.callback)

    def callback(self, msg):
        self.published = True
        self.message = msg

    def reset(self):
        self.published = False
        self.mesage = Image()
