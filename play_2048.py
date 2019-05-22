import requests
import multiprocessing as mp

# Current available algorithms
from algorithms import alg_random, alg_random_half, db_expectimax, mc, sneakyai
from util import evaluate

official_url = "https://thegame-2048.herokuapp.com"
testing_url = "http://localhost:5000"

DEBUG = False

if DEBUG:
    base_URL = testing_url
else:
    base_URL = official_url

# Number of concurrent sessions/games
TEST_NUMBER = 1
TEAM_NAME = "menyétek"
maps = {}

# Initiate algorithm configuration
BEST_ALG = sneakyai.algorithm

# Algorithm chooser
applied_algs = [BEST_ALG] * TEST_NUMBER

uIds = [0] * TEST_NUMBER


def initiate_game(table_index):
    """
    Initializes a new game instance on the server. Refreshes local data to apply the returned game board.
    :param table_index: The ID of the active game slot
    :return: None
    """
    if DEBUG:
        print("***** DEBUG MODE IS ON *****")

    try:
        # TODO: "random" should be the name of the algorithm
        SESSION_NAME = TEAM_NAME + "_" + applied_algs[table_index].label

        if DEBUG:
            request = requests.get(url=base_URL + "/api/new_game")
        else:
            request = requests.post(url=base_URL + "/api/new_game",
                                    json={"team_name": SESSION_NAME})

        print(f"Start game on table {table_index} as {SESSION_NAME}")
        print(request.text)

        maps[table_index] = request.json()['board']
        uIds[table_index] = request.json()['uId']
        request.close()

    except Exception as e:
        print(f"error in{table_index}")
        print(e)


# function to simulate play
def start_game(table_index):
    """
    Starts a game play on the table_index-th board.
    The game will be self-healing: if game_over is True, then initializes a new board and starts to play.
    :param table_index: the index of the concurrent boards
    :return: None
    """
    initiate_game(table_index)

    uId = uIds[table_index]
    current_map = maps[table_index]
    current_alg = applied_algs[table_index].func
    game_over = False

    while True:
        if not game_over:
            # print('Move scores')
            # print(evaluate.evaluate(current_map, 0))
            # print(evaluate.evaluate(current_map, 1))
            # print(evaluate.evaluate(current_map, 2))
            # print(evaluate.evaluate(current_map, 3))

            move = current_alg(current_map)

            # previousmoves = []
            # print(previousmoves)
            # # check for bug
            # # first case
            # if len(previousmoves) == 0:
            #     previousmoves.append(move)
            # # same movement
            # elif previousmoves[-1] == move:
            #     previousmoves.append(move)
            # # 10 same movement
            # elif len(previousmoves) == 10:
            #     wrongdirection = previousmoves[-1]
            #     previousmoves = []
            #     moves = ["right", "left", "up", "down"]
            #     moves.remove(wrongdirection)
            #
            #     move = random.choice(directions)

            print(move)

            request = requests.post(url=base_URL + "/api/play_the_game",
                                    json={'direction': move,
                                          'uId': uId})

            current_map = request.json()['board']

            print(request.json())

            # TODO: Type checking, error handling (HTTP response?)
            game_over = request.json()["game_over"]

        else:
            initiate_game(table_index)
            game_over = False
            uId = uIds[table_index]
            current_map = maps[table_index]


# Initialize parallel games
pool = mp.Pool(mp.cpu_count())
results = pool.map(start_game, range(TEST_NUMBER))
pool.close()
print(results)
