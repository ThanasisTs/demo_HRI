cmake_minimum_required(VERSION 2.8.3)
project(demo_HRI)


find_package(catkin REQUIRED COMPONENTS
  movement_detection
  roscpp
  rospy
  geometry_msgs
  manos_gazebo
  control_trajectory_execution
  trajectory_custom_msgs
  actionlib
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES demo_HRI
#  CATKIN_DEPENDS movement_detection roscpp rospy trajectory_process_utils
#  DEPENDS system_lib
)

include_directories(
	include
  	${catkin_INCLUDE_DIRS}
)

add_executable (control_trajectory_execution_action_client src/control_trajectory_execution_action_client.cpp)
target_link_libraries (control_trajectory_execution_action_client ${catkin_LIBRARIES})
