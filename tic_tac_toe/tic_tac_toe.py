# 1. Tic-tac-toe
# Write a function move that accepts three arguments:

# board - a 2-dimensional array that represents a 3x3 tic-tac-toe board
# location - a 2-item tuple that specifies an cell on the board
# player - a String, either "X" or "Y"
# 
# Return a copy of the board with the player String placed at the location.

# Throw an error if:

# The board is the wrong size
# The location is already occupied by a player
# The location is invalid
# The player String is something other than "X" or "Y"

# tuple is a list you can't change the values in ()
# loc = location

def print_board(board):
    for row in board:
        print(row)
        # for column in row:
        #     print(column)

def is_valid_size(board):
    # 1. Setup/Configuration
    is_valid = True

    # 2. Do some work
    # Does it have 3 rows?
    if len(board) !=3:
        is_valid = False
    for row in board:
        if len(row) != 3:
            is_valid = False    

    # Return the result
    return is_valid

def move(board, location, player): 
    # Handle those errors
    if not is_valid_size(board):
        raise Exception("Game board size is not valid")
    
    # print(f"The Player is {player}")
    row_number = location[0]
    col_number = location[1]
    # print(f"They want to move to row {row_number}")
    # print(f"They want to move to column {column_number}")
    
    board[row_number][col_number] = player
    # print(board)
    return board
    
game_board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# print(is_valid_size(game_board))

player = "O"
loc = (0, 0)
game_board = move(game_board, loc, player)

player = "X"
loc = (0, 1)
game_board = move(game_board, loc, player)

print_board(game_board)


############

