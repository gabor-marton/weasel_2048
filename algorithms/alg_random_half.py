from algorithms import alg_class
from util import evaluate


def alg(game_board):
    movetypes = ("w", "a")

    if evaluate.evaluate(game_board, 0) == -1 and evaluate.evaluate(game_board, 1) == -1:
        # Standard steps are deadlocks
        if evaluate.evaluate(game_board, 2) > evaluate.evaluate(game_board, 3):
            return "d"
        else:
            return "s"
    else:
        if evaluate.evaluate(game_board, 0) > evaluate.evaluate(game_board, 1):
            return "a"
        else:
            return "w"


algorithm = alg_class.Algorithm(label="oriented", func=alg)
