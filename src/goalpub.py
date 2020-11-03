#!/usr/bin/python

import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

rospy.wait_for_service('/motor_on')
rospy.wait_for_service('/motor_off')
rospy.on_shutdown(rospy.ServiceProxy('/motor_off',Trigger).call)
rospy.ServiceProxy('/motor_on',Trigger).call()

rospy.init_node('goal_topic_publisher')
pub = rospy.Publisher('/move_base/goal',MoveBaseActionGoal,queue_size=5)


rate = rospy.Rate(10)

me = MoveBaseActionGoal()
me.goal.target_pose.header.frame_id = "map"
me.goal.target_pose.pose.position.x = 1.0
me.goal.target_pose.pose.orientation.w = 5.0

move = Twist()
move.linear.x = -1

while not rospy.is_shutdown():
    me.header.stamp = rospy.Time.now()
    me.goal.target_pose.header.stamp = rospy.Time.now()
    pub.publish(me)
    rate.sleep()
