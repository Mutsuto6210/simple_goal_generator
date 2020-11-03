#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger,TriggerResponse

rospy.wait_for_service('/motor_on')
rospy.wait_for_service('/motor_off')
rospy.on_shutdown(rospy.ServiceProxy('/motor_off',Trigger).call)
rospy.ServiceProxy('motor_on',Trigger).call()

rospy.init_node('secmove')
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)

vel = Twist()
vel.linear.x = 10
rospy.sleep(2.0)
vel.angular.z = 3.14/4
rospy.sleep(2.0)
vel.linear.x = -10
