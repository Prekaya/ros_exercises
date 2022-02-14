#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import math


def open_space_publisher():
    rospy.init_node('open_space_publisher', anonymous=True)
    rospy.Subscriber("fake_scan", LaserScan, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def callback(data):
    os_distance = rospy.Publisher('open_space.distance', Float32, queue_size=10)
    os_angle = rospy.Publisher('open_space.angle', Float32, queue_size=10)
    os_distance_out = max(data.data.ranges)
    os_angle_out = data.data.angle_min + (data.data.angle_increment * data.data.ranges.index(os_distance_out))
    rospy.loginfo(os_angle_out)
    os_distance.publish(os_distance_out)
    os_angle.publish(os_angle_out)

if __name__ == '__main__':
    open_space_publisher()