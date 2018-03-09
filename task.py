

import random
import sys

class FlightSimulator:

	def __init__(self, angle = 0.0):
		self.angle = angle


	def print_orientation(self):
		print "Current orientation is: {}".format(self.angle)

	def proper_angle(self):
		return 45.0


i=0

while True:
	
	if input ("Do you want to end the loop? Type Y for yes or N for no: ") == 'Y': 
		break
		
	else:	
		angle1 = random.randint(0, 360)
		plane = FlightSimulator(angle1)	
		plane.print_orientation()

		if plane.angle != plane.proper_angle:
			plane.angle = plane.proper_angle

		plane.print_orientation()	


		i+=1
