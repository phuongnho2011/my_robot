#! /usr/bin/env python

import rospy    

from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    regions = [
        min(msg.ranges[0:35]),
        min(msg.ranges[36:71]),
        min(msg.ranges[72:107]),
        min(msg.ranges[108:143]),
        min(msg.ranges[144:179]),
        min(msg.ranges[180:215]),
        min(msg.ranges[216:251]),
        min(msg.ranges[252:287]),
        min(msg.ranges[288:323]),
        min(msg.ranges[324:359]),
    ]
    rospy.loginfo(regions)
def main():
    rospy.init_node('reading_rplidar_laser')
    
    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)

    rospy.spin()
if __name__ == '__main__':
    main()