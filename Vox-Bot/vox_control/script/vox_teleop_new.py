#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(msg):
    global pub
    pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('cmd_vel_remapper', anonymous=True)
    pub = rospy.Publisher('/vox/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('cmd_vel', Twist, cmd_vel_callback)
    rospy.spin()