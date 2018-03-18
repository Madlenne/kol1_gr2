import random
import time
from plane import Plane
class Environment:

	def __init__(
			self, city,
			kilometers):
		self.density = 0
		self.plane = Plane()
		self.city = city
		self.kilometers = kilometers
	
	def planes_density(
			self):
		self.density = random.randint(0,30)
		radius = random.uniform(30.0, 130.0)
		if self.density > 27:
			if radius > 100.0:
				self.crash_probability = 17/20 * 100
				print ("Crash probability: {}".format(self.crash_probability))
			print("Alert!There are {0} planes within a {1:05.2f} km radius.".format(self.density, radius))
			print("Do you want to:\n1.stay on this route\n2.change the route (recommended)?")
			answer = input()
			if answer == 1:
				plane.change_route()

	def turbulations(
			self):
		turbulations_angle = random.gauss(0, 15)
		self.plane.add_angle(turbulations_angle)
		if abs(self.plane.angle) > abs(self.plane.max):
			self.crash_danger() 
		return turbulations_angle

	def crash_danger(
			self):
		print("Alert! High crash probability detected!")
		print("Immediate change of the route")
		self.plane.change_route()

	
	def airport_problem(
			self, 
			city):
		if not random.randint(0,10)%10:
			print("Alert! Landing in {} is impossible. The plane will be rerouted to the nearest airport".format(city))
			self.plane.change_route()

	def run(
			self):
		self.plane.set_angle()
		self.plane.set_kilometers(self.kilometers)
		for x in Plane():
			self.turbulations()
			self.plane.tilt_correction()
			self.plane.decrease_km()
			self.airport_problem(self.city)
			self.planes_density()
			if self.plane.left_kilometer <=0:
				print ("You've reached the destination!")
				break
			self.plane.set_answer()
			