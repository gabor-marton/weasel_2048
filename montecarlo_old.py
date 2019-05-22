import requests 
import time 
import random
import multiprocessing as mp

from engine.p2048 import Board


# NEW GAME endpoint
request = requests.get(url = "https://thegame-2048.herokuapp.com/api/new_game")

# NR of parallel games
test = 1

# to store game
games = {}

# requesting the test games
for i in range(test):
	try:
		start = time.time()
		request = requests.get(url = "https://thegame-2048.herokuapp.com/api/new_game")
		end = time.time()

		games[i] = request.json()
		end1 = time.time()
		request.close()

		print(f"get request in {end  - start}")
		print(f"get request + save map {end1 - start}")
		print(i)

	except Exception as e:
		print(e)
		print(f"error in{i}")

print(games)

# initialize games with local engine   FIRST RUN SHOULD BE DIFFERENT
local_games = {}

for i in range(test):
	# create local games
	if games[i]['c_score'] == 0:
		local_games[games[i]['uId']] = Board()
	else:
		b = Board()
		local_games[games[i]['uId']] = b.get_initstate_from_server(games[i]['board'])

# function to simulate play 
def test_game(uId):
	game_over = False
	while game_over == False :

		movetypes = ("w","a","s","d")

		# THE AI
		grid = local_games[uId]
		depth = 3

		player = 1
		board = 0

		def expectimax(grid, depth, agent):

			# last
			if depth == 0:
				return grid.score
			elif agent == player:
				score =


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

		move = random.choice(movetypes)
		print(move)
		start = time.time()
		request = requests.post(url = "https://thegame-2048.herokuapp.com/api/play_the_game",
			json = { 'direction' : move,
					'uId' : uId})
		end = time.time()
		print(f"execution time is {end-start}s")
		# game_over = request.json("game_over")
		print(request.text)



# get the Id of all game
uIds = []
for i in range(test):
	uIds.append(games[i]['uId'])


# create pools for multi threading
pool = mp.Pool(mp.cpu_count())

results = pool.map(test_game, uIds)

pool.close()

# print(results[:10])
# #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]



