import rospy
from sensor_msgs.msg import Imu

class ImuMonitor():
    def __init__(self, topic):
        self.topic = topic
        self.published = False
        self.calibrated = False
        self.data = Imu()
        
        rospy.Subscriber(topic, Imu, self.callback)

    def callback(self, data):
        self.published = True
        self.data = data

    def reset(self):
        self.published = False
        self.data = Imu()