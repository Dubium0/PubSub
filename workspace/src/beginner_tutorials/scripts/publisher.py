#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def publ():
    pub = rospy.Publisher("main",Int32,queue_size = 10)
    rospy.init_node("publ", anonymous=True)
    rate = rospy.Rate(50)
    #first 46 fibonacci line #10 times
    i = 0
    prev,now =0,1
    while not rospy.is_shutdown():
        h_tuple = now ,rospy.get_time()
        rospy.loginfo(h_tuple)
        pub.publish(now)
        rate.sleep()
        prev,now=now,now+prev
        if now == 2971215073:
            prev,now=0,1
        i+=1
        if i==46*10:
            break

        
        
        
        
if __name__ =="__main__":
    try:
        publ()
    except rospy.ROSInterruptException:
        pass