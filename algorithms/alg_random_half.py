from algorithms import alg_class
from util import evaluate


def alg(game_board):
    """
    This algorithm attempts to only use left/up commands. If nto possible, right/down are also accepted.

    :param game_board: game board array
    :return: returns the move (char)
    """
    if evaluate.evaluate(game_board, 0) == -1 and evaluate.evaluate(game_board, 3) == -1:
        # Standard steps are deadlocks
        if evaluate.evaluate(game_board, 2) > evaluate.evaluate(game_board, 1):
            return "d"
        else:
            return "w"
    else:
        if evaluate.evaluate(game_board, 0) > evaluate.evaluate(game_board, 3):
            return "a"
        else:
            return "s"


algorithm = alg_class.Algorithm(label="oriented", func=alg)
