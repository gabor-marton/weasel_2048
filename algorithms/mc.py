import requests
import time
import random
import multiprocessing as mp
import copy

from engine.p2048 import Board



# function to simulate play
def mc(serverboard):

	serverboard = serverboard['board']

	# Use local engine
	grid = Board()

	# change board
	grid.state = serverboard

	# nr of random runs
	runs = 10

	#
	games = []
	for i in range(runs):
		games.append(copy.deepcopy(grid))

	moves()
	# Initialize parallel games
	pool = mp.Pool(mp.cpu_count())
	results = pool.map(start_game, range(TEST_NUMBER))
	pool.close()
