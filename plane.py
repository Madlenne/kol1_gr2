import random
class Plane:

	directions = [
		'north', 'south',
		'east', 'west'
	]

	def __init__(
			self):
		self.answer = None
		self.angle = 0
		self.max = -25.0
		self.left_kilometer = 0

	def __iter__(
			self):
		return self

	def __next__(
			self):
		if self.set_answer() == 'y':
			raise StopIteration
		return self.angle

	def set_angle(
			self):
		self.angle = random.gauss(0, 25)

	def set_kilometers(
			self, 
			kilometers):
		self.left_kilometer = kilometers

	def add_angle(
			self, 
			new_angle):
		self.angle += new_angle

	def rand_directions(
			self):
		self.rand_direction = random.choice(self.directions)
		self.rand_km = random.uniform(0, self.left_kilometer)
                            
	def set_answer(
			self):
		CURSOR_UP_ONE = '\x1b[1A'
		ERASE_LINE = '\x1b[2K'
		self.answer = input()
		print('\t\t{0}{1}Current orientation: {2:05.2f} '.format(CURSOR_UP_ONE,ERASE_LINE, self.angle),end='\r')
		return self.answer

	def print_flight(
			self):
		self.rand_directions()
		self.temp_rest_km = self.left_kilometer - self.rand_km
		print("You are heading {0} for {1:05.2f} kilometers".format(self.rand_direction, self.temp_rest_km))
		print("Current orientation: {0:05.2f} ". format(self.angle))
		if self.left_kilometer>0:
			print("{0:05.2f} kilometers left. \n". format(self.left_kilometer))


	def decrease_km(
			self):
		if self.left_kilometer < 5000:
			self.left_kilometer -= 500.0
		elif self.left_kilometer >= 5000 and self.left_kilometer < 10000:
			self.left_kilometer -= 3000
		else:
			self.left_kilometer -= 5000

	
	def tilt_correction(
			self):
		self.correct_angle = random.uniform(0, abs(random.gauss(0, 15)))

		if self.angle > 0:
			self.angle -= self.correct_angle
		elif self.angle < 0:
			self.angle += self.correct_angle

	def change_route(
			self):
		self.rand_directions()
		added_km = random.uniform(0, self.left_kilometer/3)
		self.left_kilometer += added_km
		self.angle = random.gauss(0, 8)
		self.print_flight()