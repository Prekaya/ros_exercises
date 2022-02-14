#!/usr/bin/env python
import rospy

import tf_conversions
import math
import tf2_ros
import geometry_msgs.msg


def dynamic_tf_cam_publisher():
    rospy.init_node('dynamic_tf_cam_publisher', anonymous=False)
    br_left = tf2_ros.TransformBroadcaster()
    br_right = tf2_ros.TransformBroadcaster()
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    br_left = tf2_ros.TransformBroadcaster()
    t_left = geometry_msgs.msg.TransformStamped()

    t_left.header.stamp = rospy.Time.now()   
    t_left.header.frame_id = "base_link_get"
    t_left.child_frame_id = "left_cam"
    t_left.transform.translation.x = 0.0
    t_left.transform.translation.y = -0.05
    t_left.transform.translation.z = 0.0
    q_left = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
    t_left.transform.rotation.x = q_left[0]
    t_left.transform.rotation.y = q_left[1]
    t_left.transform.rotation.z = q_left[2]
    t_left.transform.rotation.w = q_left[3]

    br_right = tf2_ros.TransformBroadcaster()
    t_right = geometry_msgs.msg.TransformStamped()

    t_right.header.stamp = rospy.Time.now()   
    t_right.header.frame_id = "left_cam"
    t_right.child_frame_id = "right_cam"
    t_right.transform.translation.x = 0.0
    t_right.transform.translation.y = 0.1
    t_right.transform.translation.z = 0.0
    q_right = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
    t_right.transform.rotation.x = q_right[0]
    t_right.transform.rotation.y = q_right[1]
    t_right.transform.rotation.z = q_right[2]
    t_right.transform.rotation.w = q_right[3]
    rate = rospy.Rate(20.0)
    while not rospy.is_shutdown():
        br_left.sendTransform(t_left)
        br_right.sendTransform(t_right)
        try:
            t_bot = tfBuffer.lookup_transform('right_cam', 'left_cam', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
        rospy.loginfo(t_bot)
        ##transform_right = listener.lookupTransform('/right_cam', '/base_link_get', rospy.Time())


if __name__ == '__main__':
    dynamic_tf_cam_publisher()