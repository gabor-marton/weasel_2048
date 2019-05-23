from engine import p2048


def evaluate(game_board, move):
    """
    Evaluates the proposed move by returning the score difference reached by the move.

    Returns -1 if the move invalid

    :param game_board: array of arrays as in the API call
    :param move: 0, 1, 2 or 3, namely left, up, right, down

    :return: the score difference reached by the move. -1 if the move is invalid
    """
    board = p2048.Board(game_board)
    # print(board.state)

    old_state = board.state.copy()

    if move == 0:
        board.move_left()
    elif move == 1:
        board.move_up()
    elif move == 2:
        board.move_right()
    elif move == 3:
        board.move_down()
    else:
        raise IndexError('Move should be a number [0; 3]')

    if old_state == board.state:
        return -1
    else:
        return board.merge_score
