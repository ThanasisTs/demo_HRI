#!/usr/bin/env python
import rospy
import csv
import sys
from geometry_msgs.msg import Point

def main():
	rospy.init_node('trajectory_csv_example')
	pub = rospy.Publisher('raw_points', Point, queue_size=10)
	file = open(sys.argv[1], 'r')
	rd = csv.reader(file)
	rospy.sleep(0.5)
	for row in rd:
		point = Point()
		point.x = float(row[0])
		point.y = float(row[1])
		point.z = float(row[2])
		pub.publish(point)
		# print (point)
		# input()
		rospy.sleep(0.047)

	print ("Published the waypoints")


main()