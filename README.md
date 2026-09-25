cd ~/ros2_ws/src

ros2 pkg create --build-type ament_python up_mover --dependencies rclpy geometry_msgs

cd ~/ros2_ws/src/up_mover/up_mover
touch mover_node.py

'mover_node = up_mover.mover_node:main'

cd ~/ros2_ws
colcon build
source ~/.bashrc

ros2 launch robin_bringup my_robot_gazebo.launch.py

ros2 run up_mover mover_node
