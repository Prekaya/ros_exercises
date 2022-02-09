#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def simple_subscriber():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    pub = rospy.Publisher('random_float_log', Float32, queue_size=10)
    rospy.init_node('simple_subscriber', anonymous=True)
    ate = rospy.Rate(20) # 20hz
    rospy.Subscriber("simple_publisher", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    while not rospy.is_shutdown():
        rand_float_log = random.random()*10
        rospy.loginfo(rand_float_log)
        pub.publish(rand_float_log)
        rate.sleep()

if __name__ == '__main__':
    simple_subscriber()