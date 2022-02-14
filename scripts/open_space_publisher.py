#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from ros_exercises.msg import OpenSpace




def open_space_publisher():
    rospy.set_param("/open_space_publisher/subscriber_topic", 'fake_scan')
    rospy.set_param("/open_space_publisher/publisher_topic", 'open_space')
    rospy.init_node('open_space_publisher', anonymous=False)
    rospy.Subscriber(rospy.get_param("/open_space_publisher/subscriber_topic"), LaserScan, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def callback(data):
    os = OpenSpace()
    os_pub = rospy.Publisher(rospy.get_param("/open_space_publisher/publisher_topic"), OpenSpace, queue_size=10)
    os.distance = max(data.ranges)
    os.angle = data.angle_min + (data.angle_increment * data.ranges.index(os.distance))
    rospy.loginfo(5.0)
    os_pub.publish(os)

if __name__ == '__main__':
    open_space_publisher()