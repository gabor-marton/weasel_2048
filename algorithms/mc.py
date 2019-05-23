import requests
import time
import random
import multiprocessing as mp
import copy

from algorithms.term2048.board import Board
from algorithms.term2048.ia import AI

from algorithms import alg_class
from util import evaluate


def mc(serverboard):

	b = Board(serverboard=serverboard)
	print(b)
	b.cells = serverboard

	print("this shit", b.cells)

	aimove = AI.nextMove(b)

	# UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4

	if aimove == 3:
		move ="a"
	elif aimove == 1:
		move ="w"
	elif aimove == 4:
		move ="d"
	elif aimove == 2:
		move ="s"
	print(move)

	return move




algorithm = alg_class.Algorithm(label="mc", func=mc)
