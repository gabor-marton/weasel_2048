import random
from algorithms import algorithms


def alg(map):
		movetypes = ("w", "a")

		move = random.choice(movetypes)
		return move


random_alg = algorithms.Algorithm(label=[],func=alg)
