import random 

class Algorithm:
"""
class for algorithms.
label = string, name of the algorithm
func = function
"""
	def __init__(self, label, func):
		self.label = label 
		self.func = func


def alg(map):
		movetypes = ("w", "a")

		move = random.choice(movetypes)
		return move


random_alg = Algorithm(label="random",func=alg)
