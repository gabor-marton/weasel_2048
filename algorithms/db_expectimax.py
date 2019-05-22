import requests
import time
import random
import multiprocessing as mp
import copy

from engine.p2048 import Board



# function to simulate play
def db_expectimax(serverboard):


	serverboard = serverboard['board']

	# Use local engine
	grid = Board()

	# change board
	grid.state = serverboard

	# depth of the search
	# depth = 5

	BOARD = 1
	PLAYER = 0

	def expectimax(grid, depth, agent):

		# last
		if depth == 0:
			return grid.score

		elif agent == PLAYER:
			score = 0

			for i in range(0, 4):
				newGrid = copy.deepcopy(grid)
				if i == 0:
					newGrid = copy.deepcopy(grid)
					newGrid.move_left()
				elif i == 1:
					newGrid = copy.deepcopy(grid)
					newGrid.move_up()
				elif i == 2:
					newGrid = copy.deepcopy(grid)
					newGrid.move_right()
				elif i == 3:
					newGrid = copy.deepcopy(grid)
					newGrid.move_down()

				newScore = expectimax(newGrid, depth -1, BOARD)

				if newScore > score:
					score = newScore

			return score

		elif agent == BOARD:
			score = 0
			totalZeroCells = 0
			for i in range(0, 4):
				for j in range(0, 4):
					# HANDLE zero tiles
					if grid.state[i][j] == 0:
						totalZeroCells += 1

						# a 4 to zero and simulate
						newGrid = copy.deepcopy(grid)
						newGrid.state[i][j] = 4
						newScore =expectimax(newGrid, depth - 1, PLAYER)
						if newScore == 0:
							score += 0
						else:
							score += (0.2 * newScore)

						# a 2 to zero and simulate
						newGrid = copy.deepcopy(grid)
						newGrid.state[i][j] = 2
						newScore = expectimax(newGrid, depth - 1, PLAYER)
						if newScore == 0:
							score += 0
						else:
							score += (0.8 * newScore)


			# print(score)
			return score / totalZeroCells

	# get the best move
	def bestMove(grid, depth):

		score = 0

		# investigate all moves
		for i in range(0, 4):

			newGrid = copy.deepcopy(grid)

			newScore = expectimax(newGrid, depth -1, agent=BOARD)
			print(i, "NewScore", newScore)
			print(i, "Score", score)

			if newScore > score:
				bestMove = i
				score = newScore

		if bestMove == 0:
			move = "a"
		elif bestMove == 1:
			move = "w"
		elif bestMove == 2:
			move = "d"
		elif bestMove == 3:
			move = "s"

		return move

	move = bestMove(grid, 4)

	return move
