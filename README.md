# my_robot
Lidar_robot

- This is my first project about tracked_robot using Lidar and ROS

- To run this package you need to learn how to use ROS (Robot Operating System)
    + ROS tutorials: http://wiki.ros.org/ROS/Tutorials
- There are some neccesary dependences packages listed below:
    + rosserial: https://github.com/ros-drivers/rosserial.git (branch jade-devel)
    + rplidar_ros: https://github.com/Slamtec/rplidar_ros.git
    + joint_state_publisher: https://github.com/ros/joint_state_publisher.git (branch kinetic-devel)
- Some basis step for running my_robot:
    + running rosserial_node: rosrun rosserial_python serial_node.py _port:="....." (rosserial_tutorials http://wiki.ros.org/rosserial_arduino/Tutorials)