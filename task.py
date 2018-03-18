import random
from environment import Environment

cities = {
	'Barcelona' : 2011, 'Paris': 1441, 'Honolulu': 11860, 
	'Ottawa': 6489, 'PyeongChang': 7953, 'Sydney':15716, 
	'Egypt': 2955, 'Oslo': 1460, 'London': 1508
}

random_city = random.choice(list(cities.keys()));
random_distance = cities[random_city]

if __name__ == "__main__":



	print ("Welcome aboard! You are flying to {}. The total distance is {} kilometers. Have a nice flight!".format(random_city, random_distance))
	env = Environment(
	random_city, random_distance)
	print("Type y if you want to stop simulation\n")
	env.run()


