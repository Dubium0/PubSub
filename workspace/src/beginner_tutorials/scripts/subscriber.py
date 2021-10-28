#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
 
def callback(data):
    rospy.loginfo(" Fibonacci number: %s", data.data)
     
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("main", Int32, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()
