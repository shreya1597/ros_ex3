#! /usr/bin/env python

import rospy
import actionlib 
from ex12_turtle_as.msg import MoveAction, MoveGoal, MoveFeedback, MoveResult
import time 
from geometry_msgs.msg import Twist 


def callback(goal):
    #Extracting the message goals and assigning it to a variable
    dirc=goal.direction
    dur=goal.duration

    #Creating a publisher 
    pub= rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    t=Twist()

    #Movement of the robot based on the goal values
    if dirc =="FORWARD":
        t.linear.x= 0.1
        rospy.loginfo('Forward 1')
        feedback.current_state="Moving Forward"
        action_server.publish_feedback(feedback)

        time.sleep(1)
        pub.publish(t)
        time.sleep(dur)

        t.linear.x=0
        pub.publish(t)
        time.sleep(1)
        
        rospy.loginfo('Forward end')
        result.final_state = "Finished moving!"
        action_server.set_succeeded(result)
        
    elif dirc =="BACKWARD":
        t.linear.x= -0.1
        rospy.loginfo('Backward 1')

        feedback.current_state="Moving Backward"
        action_server.publish_feedback(feedback)

        time.sleep(1)
        pub.publish(t)
        time.sleep(dur)

        t.linear.x=0
        pub.publish(t)
        time.sleep(1)
        
        rospy.loginfo('Backward end')
        result.final_state = "Finished moving!"
        action_server.set_succeeded(result)
        
    else:
        rospy.loginfo('Incorrect goal: Please specify FORWARD or BACKWARD!')
        result.final_state = "Wrong INPUT"
        action_server.set_succeeded(result)
    

rospy.init_node('turtle_direc') #Initiate node

action_server = actionlib.SimpleActionServer("move_server", MoveAction, callback, auto_start = False) #Initialize an action server
action_server_name = "Move turtlebot Server" #Name the action server
action_server.start() 

feedback = MoveFeedback() #Assigning a variable to feedback 
result = MoveResult() #Assigning a variable to result 

rospy.spin()




