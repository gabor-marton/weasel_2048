import requests
import time
import multiprocessing as mp

from algorithms import alg_random, alg_random_half


request = requests.get(url="https://thegame-2048.herokuapp.com/api/new_game")
TEST_NUMBER = 1
maps = {}

# Initiate algorithm configuration
BEST_ALG = alg_random.alg
applied_algs = [BEST_ALG] * TEST_NUMBER

for i in range(TEST_NUMBER):
    try:
        start = time.time()
        request = requests.get(url="https://thegame-2048.herokuapp.com/api/new_game")
        end = time.time()

        maps[i] = request.json()
        end1 = time.time()
        request.close()

        print(f"get request{end1 - start}")
        print(i)

    except Exception as e:
        print(f"error in{i}")
        print(e)


print(maps)

uIds = []
# get the Id of all game
for i in range(TEST_NUMBER):
    uIds.append(maps[i]['uId'])


# function to simulate play
def test_game(uId):
    current_map = maps[uIds.index(uId)]
    current_alg = applied_algs[uIds.index(uId)]
    game_over = False

    while not game_over:
        move = current_alg(current_map)
        print(move)
        request = requests.post(url="https://thegame-2048.herokuapp.com/api/play_the_game",
                                json={'direction': move,
                                       'uId': uId})

        print(request.text)


pool = mp.Pool(mp.cpu_count())
results = pool.map(test_game, uIds)
pool.close()
print(results[:10])
