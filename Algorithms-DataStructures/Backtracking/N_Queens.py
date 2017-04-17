"""
@author: David Lei
@since: 17/04/2017
@modified: 

Problem:
- placing queens on a chess board so that no 2 queens threaten each other
- n queens for n rows meaning there can only be 1 queen per row.

Eg:

indexes:   0 1 2 3
        0 |0|1|0|0| 1 means a queen is placed, 0 means nothing is placed.
        1 |0|0|0|1|
        2 |1|0|0|0|
        3 |0|0|1|0|
"""


def solve(row_index, board_config, n):
    # Search by column first (exhaust a row), then row (exhaust columns fully on last row).
    if row_index >= n:  # Exhausted rows indexes.
        return False

    for col_index in range(n):
        test_place_queen = can_place_queen(row_index, col_index, board_config, n)

        if test_place_queen:  # Can place queen, go to next row, start at col 0, try place others.
            board_config[row_index][col_index] = 1
            if row_index + 1 == n:
                return True
            solved = solve(row_index + 1, board_config, n)
            if solved:
                return True
            else:
                board_config[row_index][col_index] = 0
        # Check other column indexes.
    return False  # All columns checked.


def can_place_queen(current_row, current_col, board_config, n):
    # Test can place queen in row.
    for c in range(current_col + 1, n):  # Check rightwards.
        if board_config[current_row][c] == 1:
            return False
    for c in range(0, current_col):  # Check leftwards.
        if board_config[current_row][c] == 1:
            return False

    # Test can place queen in column.
    for r in range(current_row + 1, n):  # Check downwards.
        if board_config[r][current_col] == 1:
            return False
    for r in range(0, current_row):
        if board_config[r][current_col] == 1:
            return False

    # Test top right to bottom left diagonal.

    # Go to bottom left.
    temp_row, temp_col = current_row + 1, current_col - 1
    while temp_col >= 0 and temp_row < n:
        if board_config[temp_row][temp_col] == 1:
            return False
        temp_col -= 1
        temp_row += 1

    # Go to top right.
    temp_row, temp_col = current_row - 1, current_col + 1
    while temp_row >= 0 and temp_col < n:
        if board_config[temp_row][temp_col] == 1:
            return False
        temp_col += 1
        temp_row -= 1

    # Test top left to bottom right diagonal.

    # Go to bottom right.
    temp_row, temp_col = current_row + 1, current_col + 1
    while temp_row < n and temp_col < n:
        if board_config[temp_row][temp_col] == 1:
            return False
        temp_row += 1
        temp_col += 1

    # Go to top left.
    temp_row, temp_col = current_row - 1, current_col - 1
    while temp_row >= 0 and temp_col >= 0:
        if board_config[temp_row][temp_col] == 1:
            return False
        temp_row -= 1
        temp_col -= 1
    return True  # Can place queen


# Initialise variables.
n = 13
board = [[0] * n for _ in range(n)]
start_row = 0
start_col = 0

result = solve(start_row, board, n)
print(result)

# Print board
for row in board:
    s = ""
    for c in str(row):
        if c == "1":
            s += "Q"
        elif c == "0":
            s += "-"
        else:
            s += c
    print(s)

