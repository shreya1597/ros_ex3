#! /usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python class
from geometry_msgs.msg import Twist

def my_callback(request):
    rate=rospy.Rate(0.1)

    pub= rospy.Publisher('/cmd_vel',Twist, queue_size=1) #Create a publisher object 
    tw=Twist()

    for i in range (0,4): #Code for tracing a square on gazebo 
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
        i+=1

    return EmptyResponse() # the service Response class, in this case EmptyResponse

rospy.init_node('bot_service_client') #Initialize node 
my_service = rospy.Service('/my_bot_service', Empty , my_callback) # create the Service
rospy.spin() # mantain the service open.
