# BLOCKGAME problem
# Author: JeongminCha (cjm9236@me.com)

cache = None
strategy = []

L_block = [
    [[0,0],[1,0],[1,1]],
    [[0,0],[0,1],[1,1]],
    [[0,0],[0,1],[-1,1]],
    [[0,0],[1,0],[0,1]]
]
I_block = [
    [[0,0],[1,0]],
    [[0,0],[0,1]]
]

def initial_setting():
    global strategy
    for row in range(5):
        for col in range(5):
            board = [0]
            # processing L block
            for shape in range(4):
                if L_available(board, row, col, shape):
                    strategy.append(board[0])
                    L_pop(board, row, col, shape)
            # processing I block
            for shape in range(2):
                if I_available(board, row, col, shape):
                    strategy.append(board[0])
                    I_pop(board, row, col, shape)

def index(x, y):
    return int(2 ** (x + y*5))

def empty(board, x, y):
    if (x >= 0 and x < 5) and (y >= 0 and y < 5) and (board[0] & index(x,y)) == 0:
        return True
    else:
        return False

# Checks if a 'L' block is available
def L_available(board, p, q, shape):
    # Check the block can be put in the specified location.
    for i in range(3):
        x = q + L_block[shape][i][1]
        y = p + L_block[shape][i][0]
        if empty(board, x, y) is False:
            return False
    # Add the block (by OR operation)
    for i in range(3):
        x = q + L_block[shape][i][1]
        y = p + L_block[shape][i][0]
        board[0] |= index(x,y)
    return True

# Checks if a 'I' block is available
def I_available(board, p, q, shape):
    # Check the block can be put in the specified location.
    for i in range(2):
        x = q + I_block[shape][i][1]
        y = p + I_block[shape][i][0]
        if empty(board, x, y) is False:
            return False
    # Add the block (by OR operation)
    for i in range(2):
        x = q + I_block[shape][i][1]
        y = p + I_block[shape][i][0]
        board[0] |= index(x,y)
    return True

# Pops the 'L' block
def L_pop(board, p, q, shape):
    # Delete the block (by XOR operation)
    for i in range(3):
        x = q + L_block[shape][i][1]
        y = p + L_block[shape][i][0]
        board[0] ^= index(x,y)

# Pops the 'I' block
def I_pop(board, p, q, shape):
    # Delete the block (by XOR operation)
    for i in range(2):
        x = q + I_block[shape][i][1]
        y = p + I_block[shape][i][0]
        board[0] ^= index(x,y)

# Returns True if there's a way to win in the current board condition.
def check_winning_way(board):
    ret = cache[board[0]]
    if ret != -1:
        return ret
    ret = 0
    # For every strategies about putting new block
    for new_block in strategy:
        # 1. new block is not overlapped with the existing blocks.
        # 2. failing is guranteed after the new block is added.
        if ((new_block & board[0]) == 0) and \
                (check_winning_way([new_block | board[0]]) <= 0):
            ret = 1
            break
    return ret

# Returns the number meaning marked points in board
def make_board(input):
    ret = 0
    for row in range(5):
        for col in range(5):
            ret *= 2
            if input[row][col] == '#':
                ret += 1
    return ret

if __name__ == "__main__":
    initial_setting()

    for _ in range(int(raw_input())):
        cache = [-1] * (2 ** 25)
        input = []
        for _ in range(5):
            input.append(list(raw_input()))

        result = check_winning_way([make_board(input)])
        if result > 0:
            print("WINNING")
        else:
            print("LOSING")