#!/usr/bin/env python3.5
import rospy
from sensor_msgs.msg import Imu

class Republish(object):
    # ROS initialization 
    def init(self):
        self.update_rate = 100   # Node frquency (Hz)
        self.data = Imu()
        self.dataPublished = False

        # Setup publishers & subscriber
        self.pub_imu = rospy.Publisher('/imu_data', Imu, queue_size=1)
        rospy.Subscriber('/inertial', Imu, self.callbackImu)


    def callbackImu(self, data):
        self.data = data
        self.dataPublished = True

    # Controller starter
    def run(self):
        self.init()
        r = rospy.Rate(self.update_rate)
        while True:
            try:
                if self.dataPublished:
                    self.pub_imu.publish(self.data)
                    self.dataPublished = False
            except KeyboardInterrupt:
                break
def main():
    rospy.init_node('republisher', disable_signals=True)
    republisher = Republish()
    republisher.run()


if __name__ == '__main__':
    main()
 