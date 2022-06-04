#! /usr/bin/env python

import rospy
from ex10_my_srv_msg.srv import MyServiceMsg, MyServiceMsgResponse #Import service message parameters
from geometry_msgs.msg import Twist #Import twist from geometry messages
import time

def move_bot(rad,rep): #Function for movement of the robot 
    
    #rate=rospy.Rate(0.1)
    pub= rospy.Publisher('/cmd_vel',Twist, queue_size=1) #Define publisher 
    tw=Twist()

    for i in range (4*rep):
        
        time.sleep(15)
        tw.angular.z=0.157
        pub.publish(tw)
        time.sleep(10)
        tw.angular.z=0
        pub.publish(tw)
        time.sleep(2)

        tw.linear.x= 0.1
        pub.publish(tw)
        time.sleep(rad/0.1)
        tw.linear.x=0.0
        pub.publish(tw)
        time.sleep(2)

        
        i+=1
    
    return 


def my_callback(request): #Service Callback 

    rad=request.radius
    rep=request.repetitions

    move_bot(rad,rep)
    #return MyServiceMsgResponse


rospy.init_node('multi_square') #Initialize node 
my_service = rospy.Service('/multi_square_service', MyServiceMsg, my_callback) #Creating a service 
rospy.spin()
