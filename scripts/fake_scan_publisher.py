#!/usr/bin/env python
# license removed for brevity
import rospy
import random
import math
from sensor_msgs.msg import LaserScan

def fake_scan_publisher():
    pub = rospy.Publisher('fake_scan', LaserScan, queue_size=10)
    rospy.init_node('fake_scan_publisher', anonymous=True)
    rate = rospy.Rate(20) # 20hz
    while not rospy.is_shutdown():
        scan = LaserScan()
        scan.header.stamp = rospy.get_rostime()
        scan.header.frame_id = "base_link"
        scan.angle_min = (-2.0/3.0) * math.pi
        scan.angle_max = (2.0/3.0) * math.pi
        scan.angle_increment = (1.0/300.0) * math.pi
        scan.scan_time = 0.5
        scan.range_min = 1.0
        scan.range_max = 10.0
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