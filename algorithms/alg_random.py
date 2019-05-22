import random
from algorithms import algorithms


# function to simulate play 
def alg(map):
		movetypes = ("w", "a", "s", "d")

		move = random.choice(movetypes)
		return move

random_alg = algorithms.Algorithm(label=[],func=alg)
