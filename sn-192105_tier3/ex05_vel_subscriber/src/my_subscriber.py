#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def callback(var):
    #x=var.linear.x
    print var.linear.x

rospy.init_node('vel_subscriber')
rospy.Subscriber('/cmd_vel', Twist, callback)
rospy.spin()
