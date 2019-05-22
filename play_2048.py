import requests
import multiprocessing as mp

from algorithms import alg_random, alg_random_half


request = requests.get(url="https://thegame-2048.herokuapp.com/api/new_game")
TEST_NUMBER = 1
TEAM_NAME = "menyétek"
maps = {}

# Initiate algorithm configuration
BEST_ALG = alg_random.alg
applied_algs = [BEST_ALG] * TEST_NUMBER

SESSION_NAME = TEAM_NAME + "_" + "random" + "_1"

for i in range(TEST_NUMBER):
    try:
        request = requests.post(url="https://thegame-2048.herokuapp.com/api/new_game",
                                json={"team_name": SESSION_NAME})
        print(request)
        print(request.text)

        maps[i] = request.json()
        request.close()

    except Exception as e:
        print(f"error in{i}")
        print(e)


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

        print(request.json())
        # TODO: Type checking, error handling (HTTP response?)
        game_over = request.json()["game_over"]


pool = mp.Pool(mp.cpu_count())
results = pool.map(test_game, uIds)
pool.close()
print(results[:10])
