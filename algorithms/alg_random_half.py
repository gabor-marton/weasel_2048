import random
from algorithms import alg_class


def alg(map):
    movetypes = ("w", "a")

    move = random.choice(movetypes)
    return move


algorithm = alg_class.Algorithm(label="random",func=alg)
