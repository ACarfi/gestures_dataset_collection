import rospy
from std_msgs.msg import Header

class HeaderPublisher():
    def __init__(self, topic):
        self.topic = topic
        self.seq = 0
        self.message = Header()
        self.publisher = rospy.Publisher(self.topic, Header, queue_size=1)

    def publish(self, msg_string):
        self.message = Header()
        self.message.seq = self.seq
        self.message.stamp = rospy.Time.now()
        self.message.frame_id = msg_string
        self.publisher.publish(self.message)
        self.seq = self.seq + 1