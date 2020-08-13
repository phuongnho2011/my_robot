#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    # 720 / 5 = 144
    # regions = [
    #     min(min(msg.ranges[0:143]), 10),
    #     min(min(msg.ranges[144:287]), 10),
    #     min(min(msg.ranges[288:431]), 10),
    #     min(min(msg.ranges[432:575]), 10),
    #     min(min(msg.ranges[576:713]), 10),
    # ]
    # rospy.loginfo(regions)
    regions = {
        '0': min(msg.ranges[0:35]),
        '1': min(msg.ranges[36:71]),
        '2': min(msg.ranges[72:107]),
        '3': min(msg.ranges[108:143]),
        '4': min(msg.ranges[144:179]),
        '5': min(msg.ranges[180:215]),
        '6': min(msg.ranges[216:251]),
        '7': min(msg.ranges[252:287]),
        '8': min(msg.ranges[288:323]),
        '9': min(msg.ranges[324:359]),
    }
    rospy.loginfo(regions)

def main():
    rospy.init_node('reading_laser')
    
    sub = rospy.Subscriber('/myrobot/laser/scan', LaserScan, clbk_laser)
    
    rospy.spin()

if __name__ == '__main__':
    main()
