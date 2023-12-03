#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import datetime

def callback(data):
    received_msg = data.data
    signature = "Maciej Krakowiak"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    signed_msg = f"{received_msg} / {signature} / {timestamp}"

    
    pub.publish(signed_msg)
    rospy.loginfo(f"Odebrano i wysłano: {signed_msg}")

def listener():
    rospy.init_node('krakowiak_node', anonymous=True)

    rospy.Subscriber("RaptorIN", String, callback)


    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('RaptorOUT', String, queue_size=10)
    listener()
