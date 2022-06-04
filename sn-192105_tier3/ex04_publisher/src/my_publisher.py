#!/usr/bin/env python

import rospy                            
from geometry_msgs.msg import Twist          #Import the Int32 message from the std_msgs

rospy.init_node('vel_publisher')      #Initiate a Node named 'vel_publisher'
pub = rospy.Publisher('/cmd_vel', Twist) #Create a Publisher object, that will publish messages of type Twist
var=Twist()
var.linear.x=0.1  

rate = rospy.Rate(2)                    # Set a publish rate of 2 Hz

while not rospy.is_shutdown():          # Create a loop that will go until someone stops the programm
    pub.publish(var)                  # Publish the message within the 'count' variable
    rate.sleep()
