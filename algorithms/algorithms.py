import random 

class Algorithm:

	def __init__(self, label, func):
		self.label = label
		self.func = func


def alg(map):
		movetypes = ("w", "a")

		move = random.choice(movetypes)
		return move


random_alg = algorithms.Algorithm(label="random",func=alg)
		