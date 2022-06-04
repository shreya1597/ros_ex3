#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('move-turtlebot_square')
rate=rospy.Rate(0.1)

pub= rospy.Publisher('/cmd_vel',Twist, queue_size=1)
tw=Twist()

while not rospy.is_shutdown():
    tw.linear.x=0.1
    pub.publish(tw)
    rate.sleep()
    tw.linear.x=0.0
    pub.publish(tw)
    rate.sleep()

    tw.angular.z=0.157
    pub.publish(tw)
    rate.sleep()
    tw.angular.z=0
    pub.publish(tw)
    rate.sleep()

    
