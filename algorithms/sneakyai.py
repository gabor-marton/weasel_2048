import math

from algorithms.sneakyaiGAME import *
from algorithms import alg_class
from util import evaluate


from algorithms import alg_random_half

def aimove(b):
    """
    Evaluate the utility of each of the four possible moves
    we can make on b

    Args: b (list) root board to score

    Returns: list
    """

    def fitness(b):
        """
        Returns the heuristic value of b

        Snake refers to the "snake line pattern" (http://tinyurl.com/l9bstk6)
        Here we only evaluate one direction; we award more points if high valued tiles
        occur along this path. We penalize the board for not having
        the highest valued tile in the lower left corner

        Args: b (list) board to score

        Returns: float
        """

        if not move_exists(b):
            return -float("inf")

        snake = []
        for i, col in enumerate(zip(*b)):
            snake.extend(reversed(col) if i % 2 == 0 else col)

        m = max(snake)
        return sum(x/10**n for n, x in enumerate(snake)) - \
               math.pow((b[3][0] != m)*abs(b[3][0] - m), 2)

    def search(b, d, move=False):
        """
        Performs expectimax search on a given configuration to
        specified depth (d).

        Algorithm details:
           - if the AI needs to move, make each child move,
             recurse, return the maximum fitness value
           - if it is not the AI's turn, form all
             possible child spawns, and return their weighted average
             as that node's evaluation

        Args:
            b (list) board to search
            d (int) depth to serach to
            move (bool) whether or not it's our (AI player's) move to make

        Returns: float
        """

        if d == 0 or (move and not move_exists(b)):
            return fitness(b)

        alpha = fitness(b)
        if move:
            for _, action in MERGE_FUNCTIONS.items():
                child = action(b)
                alpha = max(alpha, search(child, d-1))
        else:
            alpha = 0
            zeros = [(i,j) for i, j in itertools.product(range(4), range(4)) if b[i][j] == 0]
            for i, j in zeros:
                c1 = [[x for x in row] for row in b]
                c2 = [[x for x in row] for row in b]
                c1[i][j] = 2
                c2[i][j] = 4
                alpha += (.8*search(c1, d-1, True)/len(zeros) +
                          .2*search(c2, d-1, True)/len(zeros))
        return alpha

    results = []
    for direction, action in MERGE_FUNCTIONS.items():
        result = direction, search(action(b), 4)
        results.append(result)
    return results

def aiplay(current_map):
    """
    Runs a game instance playing the move that determined
    by aimove.

    Args: game (Game) to play

    Returns: void
    """
    # print(serverboard)
    b = Game(serverboard=current_map)
    print(b)
    # while True:
    # print(str(game) + '\n')
    direction = max(aimove(b.board), key = lambda x: x[1])[0]
    print(direction)

    if direction == "left":
        if evaluate.evaluate(current_map, 0) >= 0:
            move = "a"
        else:
            print("OVERRIDE")
            move = alg_random_half.algorithm.func(current_map)
    elif direction == "up":
        if evaluate.evaluate(current_map, 0) >= 0:
            move = "w"
        else:
            print("OVERRIDE")
            move = alg_random_half.algorithm.func(current_map)
    elif direction == "right":
        if evaluate.evaluate(current_map, 0) >= 0:
            move = "d"
        else:
            print("OVERRIDE")
            move = alg_random_half.algorithm.func(current_map)
    elif direction == "down":
        if evaluate.evaluate(current_map, 0) >= 0:
            move = "s"
        else:
            print("OVERRIDE")
            move = alg_random_half.algorithm.func(current_map)

    return move


algorithm = alg_class.Algorithm(label="sneakyai", func=aiplay)
