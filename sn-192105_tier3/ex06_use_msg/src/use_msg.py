#!/usr/bin/env python

import rospy
from ex06_age_msg.msg import Age

rospy.init_node('use_msg')

a=Age()
a.years=22
a.months=11
a.days=1

print(a)