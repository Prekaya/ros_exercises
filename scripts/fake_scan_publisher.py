#!/usr/bin/env python
# license removed for brevity
import rospy
import random
import math
from sensor_msgs.msg import LaserScan

def fake_scan_publisher():
    rospy.set_param("/fake_scan_publisher/publish_topic", 'fake_scan')
    rospy.set_param("/fake_scan_publisher/publish_rate", 20)
    rospy.set_param("/fake_scan_publisher/angle_min", (-2.0*math.pi)/3.0)
    rospy.set_param("/fake_scan_publisher/angle_max", (2.0*math.pi)/3.0)
    rospy.set_param("/fake_scan_publisher/angle_increment", (math.pi/300.0))
    rospy.set_param("/fake_scan_publisher/range_min", 1.0)
    rospy.set_param("/fake_scan_publisher/range_max", 10.0)


    pub = rospy.Publisher(rospy.get_param("/fake_scan_publisher/publish_topic"), LaserScan, queue_size=10)
    rospy.init_node('fake_scan_publisher', anonymous=True)
    rate = rospy.Rate(rospy.get_param("/fake_scan_publisher/publish_rate")) # 20hz
    while not rospy.is_shutdown():
        scan = LaserScan()
        scan.header.stamp = rospy.get_rostime()
        scan.header.frame_id = "base_link"
        scan.angle_min = rospy.get_param("/fake_scan_publisher/angle_min")
        scan.angle_max = rospy.get_param("/fake_scan_publisher/angle_max")
        scan.angle_increment = rospy.get_param("/fake_scan_publisher/angle_increment")
        scan.scan_time = 0.5
        scan.range_min = rospy.get_param("/fake_scan_publisher/range_min")
        scan.range_max = rospy.get_param("/fake_scan_publisher/range_max")
        x_range = int((scan.angle_max - scan.angle_min)/scan.angle_increment)
        scan.ranges = [(random.random()*(scan.range_max-scan.range_min) + scan.range_min) for _ in xrange(x_range)]
        #rospy.loginfo(len(scan.ranges))
        pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_scan_publisher()
    except rospy.ROSInterruptException:
        pass