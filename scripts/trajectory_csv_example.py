#!/usr/bin/env python
import rospy
import csv
import sys
from geometry_msgs.msg import Point
from visualization_msgs.msg import Marker

def main():
	rospy.init_node('trajectory_csv_example')
	pub = rospy.Publisher('raw_points', Point, queue_size=10)
	vis_pub = rospy.Publisher('visualization_human', Marker, queue_size=10)
	file = open(sys.argv[1], 'r')
	rd = csv.reader(file)
	rospy.sleep(0.05)
	marker = Marker()
	marker.header.frame_id = "base_link"
	marker.header.stamp = rospy.Time.now()
	marker.action = marker.ADD
	marker.type = marker.LINE_STRIP
	marker.pose.position.x = 0
	marker.pose.position.y = 0
	marker.pose.position.z = 0
	marker.pose.orientation.x = 0
	marker.pose.orientation.y = 0
	marker.pose.orientation.z = 0
	marker.pose.orientation.w = 1
	marker.scale.x = 0.01
	marker.color.a = 1.0
	marker.color.r = 1.0
	marker.color.g = 0.0
	marker.color.b = 0.0
	marker.lifetime = rospy.Duration(100)

	for row in rd:
		point = Point()
		point.x = float(row[0])
		point.y = float(row[1])
		point.z = float(row[2])
		pub.publish(point)
		# print (point)
		# input()
		marker.points.append(point)
		rospy.sleep(0.047)
	vis_pub.publish(marker)
	print ("Published the waypoints")


main()