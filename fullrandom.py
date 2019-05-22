import requests 
import time 
import random
import multiprocessing as mp


request = requests.get(url = "https://thegame-2048.herokuapp.com/api/new_game")
test = 10
maps = {}

for i in range(test):
	try:
		start = time.time()
		request = requests.get(url = "https://thegame-2048.herokuapp.com/api/new_game")
		end = time.time()

		maps[i] = request.json()
		end1 = time.time()
		request.close()

		print(f"get request in {end  - start}")
		print(f"get request + save map {end1 - start}")
		print(i)

	except Exception as e:
		print(e)
		print(f"error in{i}")


print(maps)

uIds = []
# get the Id of all game 
for i in range(test):
	uIds.append(maps[i]['uId'])


# function to simulate play 
def test_game(uId):
	game_over = False
	while game_over == False : 
		movetypes = ("w","a","s","d")
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


pool = mp.Pool(mp.cpu_count())

results = pool.map(test_game, uIds)

pool.close()

print(results[:10])
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]



