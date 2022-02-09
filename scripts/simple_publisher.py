#!/usr/bin/env python
# license removed for brevity
import rospy
import random
from std_msgs.msg import Float32

def simple_publisher():
    pub = rospy.Publisher('my_random_float', Float32, queue_size=10)
    rospy.init_node('simple_publisher', anonymous=True)
    rate = rospy.Rate(20) # 20hz
    while not rospy.is_shutdown():
        rand_float = random.random()*10
        rospy.loginfo(rand_float)
        pub.publish(rand_float)
        rate.sleep()

if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInterruptException:
        pass