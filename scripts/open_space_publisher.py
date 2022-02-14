#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from ros_exercises.msg import OpenSpace


def open_space_publisher():
    rospy.init_node('open_space_publisher', anonymous=False)
    rospy.Subscriber("fake_scan", LaserScan, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def callback(data):
    os = OpenSpace()
    os_pub = rospy.Publisher('open_space', OpenSpace, queue_size=10)
    os.distance = max(data.ranges)
    os.angle = data.angle_min + (data.angle_increment * data.ranges.index(os.distance))
    #rospy.loginfo(os_angle_out)
    os_pub.publish(os)

if __name__ == '__main__':
    open_space_publisher()