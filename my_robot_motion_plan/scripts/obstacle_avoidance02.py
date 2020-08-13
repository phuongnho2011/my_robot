#! /usr/bin/env python

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import rospy

safe_distance_rl = 0.52
safe_distance_f = 0.5
safe_distance_right = 0.3
safe_distance_brl = 0.3

pub = None


def clbk_laser(msg):
    regions = {
        # 'front': min(min(msg.ranges[0:22]), min(msg.ranges[337:359])),
        # 'frontr': min(msg.ranges[314:336]),
        # 'frontl': min(msg.ranges[23:45]),
        # 'right': min(msg.ranges[223:313]),
        # 'left': min(msg.ranges[46:135]),
        # 'backr': min(msg.ranges[202:224]),
        # 'backl': min(msg.ranges[136:158]),
        # 'back': min(min(msg.ranges[180:202]), min(msg.ranges[158:181])),
        
        'front': min(min(msg.ranges[0:22]), min(msg.ranges[337:359])),
        'frontr': min(msg.ranges[314:336]),
        'frontl': min(msg.ranges[23:45]),
        'right': min(msg.ranges[243:293]),
        'left': min(msg.ranges[66:115]),
        'backr': min(msg.ranges[202:244]),
        'backl': min(msg.ranges[116:158]),
        'back': min(min(msg.ranges[180:202]), min(msg.ranges[158:181])),
    }
    take_action(regions)


def take_action(regions):
    msg = Twist()
    linear_x = 0
    angular_z = 0

    state_description = ''

    if regions['front'] > safe_distance_f and regions['frontl'] > safe_distance_rl and regions['frontr'] > safe_distance_rl:
        state_description = 'case 1 - Forward'
        linear_x = 0.25
        angular_z = 0
        rospy.loginfo(regions)
    elif regions['front'] > safe_distance_f and regions['frontl'] > safe_distance_rl  and regions['frontr'] < safe_distance_rl:
        state_description = 'case 2 - Solf_left'
        linear_x = 0.15
        angular_z = 1.4
        rospy.loginfo(regions)
    elif regions['front'] < safe_distance_f and regions['frontl'] > safe_distance_rl  and regions['frontr'] < safe_distance_rl:
        state_description = 'case 3 - Solf_left'
        linear_x = 0
        angular_z = 2
        rospy.loginfo(regions)
    if regions['front'] > safe_distance_f and regions['frontl'] > safe_distance_rl and regions['frontr'] > safe_distance_rl and regions['right'] < safe_distance_right:
        state_description = 'case 4 - Hard_left'
        linear_x = 0.1
        angular_z = 2
        rospy.loginfo(regions)
    if regions['front'] > safe_distance_f and regions['frontl'] > safe_distance_rl and regions['frontr'] > safe_distance_rl and regions['backr'] < safe_distance_brl:
        state_description = 'case 5 - Hard_right'
        linear_x = 0.25 
        angular_z = -0.75
        rospy.loginfo(regions)
    if regions['front'] < safe_distance_f and regions['frontl'] > safe_distance_rl and regions['frontr'] < safe_distance_rl:
        state_description = 'case 6 - Hard_left'
        linear_x = 0
        angular_z = 2
        rospy.loginfo(regions)
    if regions['front'] < safe_distance_f and regions['frontl'] < safe_distance_rl and regions['frontr'] < safe_distance_rl:
        state_description = 'case 7 - Backward'
        linear_x = -0.2
        angular_z = 0
        rospy.loginfo(regions)
    if regions['front'] < safe_distance_f and regions['frontl'] > safe_distance_rl and regions['frontr'] > safe_distance_rl:
        state_description = 'case 8  - Hard_left'
        linear_x = 0
        angular_z = 2
        rospy.loginfo(regions)
    # elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] > 1:
    #     state_description = 'case 4 - fleft'
    #     linear_x = 0
    #     angular_z = -0.3
    # elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] < 1:
    #     state_description = 'case 5 - front and fright'
    #     linear_x = 0
    #     angular_z = 0.3
    # elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] > 1:
    #     state_description = 'case 6 - front and fleft'
    #     linear_x = 0
    #     angular_z = -0.3
    # elif regions['left1'] > 1:
    #     state_description = 'new case - left1'
    #     linear_x = 0.1
    #     angular_z = 0.1
    # elif regions['right'] > 1:
    #     state_description = 'new case - right1'
    #     linear_x = 0.1
    #     angular_z = -0.1
    # elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] < 1:
    #     state_description = 'case 7 - front and fleft and fright'
    #     linear_x = 0.1
    #     angular_z = 0.1
    # elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] < 1:
    #     state_description = 'case 8 - fleft and fright'
    #     linear_x = 0.1
    #     angular_z = 0
    # if:
    #     state_description = 'unknown case'
    #     linear_x = 0
    #     angular_z = 0
    #     rospy.loginfo(regions)
    
    rospy.loginfo(state_description)
    rospy.loginfo(regions)
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub.publish(msg)


def main():
    global pub

    rospy.init_node('reading_laser')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)

    rospy.spin()


if __name__ == '__main__':
    main()
