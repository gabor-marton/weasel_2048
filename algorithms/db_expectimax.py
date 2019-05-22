import requests
import time
import random
import multiprocessing as mp
import copy
from engine.p2048 import Board



# function to simulate play 
def db_expectimax(board):


	movetypes = ("w","a","s","d")

	# Use local engine
	grid = Board()
	grid = grid.get_initstate_from_server(board)

	# depth of the search
	depth = 3

	PLAYER = 1
	BOARD = 0

	def expectimax(grid, depth, agent):

		# last
		if depth == 0:
			return grid.score

		elif agent == PLAYER:
			score = 0

			for i in range(0, 4):
				newGrid = copy.de
				if i == 0:
					newGrid = grid.clone()
					nextLevel = grid.move_right
				elif i == 1:
					newGrid = grid.clone()
					nextLevel = grid.move_left
				elif i == 2:
					newGrid = grid.clone()
					nextLevel = grid.move_up
				elif i == 3:
					newGrid = grid.clone()
					nextLevel = grid.move_down

				newScore = expectimax(newGrid, depth -1, BOARD)

				if newScore > score:
					score = newScore

			return score

		elif agent == BOARD:
			score = 0
			for i in range(0, 4):
				for j in range(0,4):
					if grid[i][j] == 0:
						newGrid = grid.clone()
						newGrid


	# get the best move
	def bestMove(grid, depth):

		score = 0
		bestMove = []

		# investigate all moves
		for i in range(0, 4):

			newGrid = grid.clone()

			newScore = expectimax(newGrid, depth -1, board)

			if newScore > score:
				bestmove = i
				score = newScore


	move = 0

	return move

