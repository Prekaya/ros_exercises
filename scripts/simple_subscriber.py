#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import math


    
def simple_subscriber():
    rospy.init_node('simple_subscriber', anonymous=True)
    rospy.Subscriber("my_random_float", Float32, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def callback(data):
    log_pub = rospy.Publisher('random_float_log', Float32, queue_size=10)
    rand_float_log = math.log(data.data)
    #rospy.loginfo(rand_float_log)
    log_pub.publish(rand_float_log)

if __name__ == '__main__':
    simple_subscriber()