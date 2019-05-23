from functools import partial
import random
import copy


class GameOverException(Exception):
    def __init__(self, board):
        self.score = board.score


def board_move(move_func):
    def wrapper(*args, **kwargs):
        board = args[0]
        board.move_count += 1
        return_value = move_func(*args, **kwargs)

        return return_value
    return wrapper


class Board(object):
    """
    Represents a 4x4 game board
    """

    def __init__(self, state=None):
        self.merge_score = 0
        if state is None:
            self.state = self._get_random_init_state()
        else:
            self.state = state
        self.move_count = 0


    def get_initstate_from_server(self, serverboard):
        """
        Initialize a board with a given board
        """
        for i in range(0, 4):
            for j in range(0, 4):
                self.state[i][j] = serverboard[i][j]

    def _get_random_init_state(self):
        """
        Returns an initial board state with everything being zeroes except
        two '2's
        """
        initial_board = [0]*16
        for index in random.sample(range(16), 2):
            initial_board[index] = 2
        return self.deserialize(initial_board)

    def serialize(self):
        """
        Returns the serialized state of the board being the rows joined
        into one flat list
        """
        return sum(self.state, [])

    def deserialize(self, flat_list):
        """
        Returns a 'deserialized' board state from the given flat list
        """
        split_indices = map(lambda x: 4*x, range(4))
        return [flat_list[index:index+4] for index in split_indices]

    def rotate(self):
        """
        self.rotates the board by 90 deegrees clockwise
        """
        self.state = self.rotate(self.state)

    @board_move
    def move_left(self):
        """
        Performs the 'left' move on the board, increments the move counter and
        adds a new random element
        """
        self._move_left()

    def _move_left(self):
        """
        Performs the 'left' move on the board
        """
        self.apply([partial(map, self.move)])

    @board_move
    def move_right(self):
        """
        Performs the 'right' move on the board, increments the move counter and
        adds a new random element
        """
        self._move_right()

    def _move_right(self):
        """
        Performs the 'right' move on the board
        """
        self.apply([self.rotate, self.rotate, partial(map, self.move), self.rotate, self.rotate])

    @board_move
    def move_down(self):
        """
        Performs the 'down' move on the board, increments the move counter and
        adds a new random element
        """
        self._move_down()

    def _move_down(self):
        """
        Performs the 'down' move on the board
        """
        self.apply([self.rotate, partial(map, self.move), self.rotate, self.rotate, self.rotate])

    @board_move
    def move_up(self):
        """
        Performs the 'up' move on the board, increments the move counter and
        adds a new random element
        """
        self._move_up()

    def _move_up(self):
        """
        Performs the 'up' move on the board
        """
        self.apply([self.rotate, self.rotate, self.rotate, partial(map, self.move), self.rotate])

    def apply(self, functions):
        """
        Applies the list of functions to the board's state in the given order
        """
        state = list(self.state)
        for function in functions:
            state = function(state)
        self.state = list(state)

    def __repr__(self):
        return '<Board {}>'.format(self.state)


    @property
    def score(self):
        """
        Returns the Board's score
        """
        return sum(self.serialize())

    def merge(self, row):
        result = []
        row = list(row)  # copy the row
        row.reverse()
        digit_stack = row
        while digit_stack:
            if len(digit_stack) == 1:
                result.append(digit_stack.pop())
                break
            a = digit_stack.pop()
            b = digit_stack.pop()
            if a == b:
                result.append(a + b)
                self.merge_score += a + b
            else:
                result.append(a)
                digit_stack.append(b)
        return result


    def move(self, row):
        without_zeroes = filter(bool, row)
        return self.right_pad(self.merge(without_zeroes))
    
    
    def right_pad(self, input_list, size=4):
        result = input_list[:]
        extension = [0, ] * (size - len(result))
        result.extend(extension)
        return result
    
    
    def rotate(self, board):
        """
        Returns the given board rotated by 90 degrees clockwise.
        """
        board = list(board)  # copy the board
        board.reverse()
        rotated_board = map(list, zip(*board))
        return list(rotated_board)
