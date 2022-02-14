#!/usr/bin/env python
import rospy
import tf
import tf2_msgs
import tf2_ros
import numpy as np
import geometry_msgs.msg
from std_msgs.msg import Float32


    
def dynamic_tf_cam_publisher():
    rospy.init_node('dynamic_tf_cam_publisher', anonymous=False)
    br_left = tf.TransformBroadcaster()
    br_right = tf.TransformBroadcaster()
    tfBuffer = tf2_ros.Buffer()
    listener = tf.TransformListener(tfBuffer)
    
    while not rospy.is_shutdown():
        br_left.sendTransform((0.0, -0.05, 0.0),(0.0, 0.0, 0.0, 1.0),rospy.Time.now(),
                            "left_cam",
                            "base_link_get")
        br_right.sendTransform((0.0, 0.05, 0.0),(0.0, 0.0, 0.0, 1.0),rospy.Time.now(),
                            "right_cam",
                            "base_link_get")
        try:
            (t_bot, r_bot) = listener.lookupTransform('/base_link_get', '/world', rospy.Time.now())
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rospy.loginfo(5.0)
        ##transform_right = listener.lookupTransform('/right_cam', '/base_link_get', rospy.Time())


if __name__ == '__main__':
    dynamic_tf_cam_publisher()