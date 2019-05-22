import random

from algorithms import alg_class
from util import evaluate

commands = {
	"0": "a",
	"1": "w",
	"2": "d",
	"3": "s"
}


def alg(game_board):
	"""
	The algorithm picks a random but possible move

	:param map:
	:return:
	"""
	try:
		move = random.choice([commands[x] for x in commands.keys() if evaluate.evaluate(game_board, int(x)) >= 0])
	except Exception:
		move = "a"

	return move


algorithm = alg_class.Algorithm(label="random", func=alg)
