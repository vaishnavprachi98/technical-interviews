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

Complexity analysis

TODO: Clean up complexity analysis.

Time Complexity:
- Best: Placement always works, O(n) for n rows.
- Worst: (Guess)

    For n = 4.
        After placing the first queen in the first row, there are another n-1 (3) queens to place.
        After placing the 2nd queen in the second row, there are another n-2 (2) queens to place.
        This goes on until all n (4) queens are placed. This is n work.

        After placing each queen and moving on to the next row, backtracking may occur. Once the first queen is placed,
        if backtracking occurs there is an upper bound of another n-1 options to consider.

    After placing a queen, there are n-1 options left in that row.
    There are also n - 1 - placed_queens rows left to assign to a queen.
    This can be done all the way until the end at which there may be a backtrack all the way to the start which can occur n - 1 times.

    n work to place n queens in some configuration with considering n columns = n * n.

    backtracking to the first row can happen  = (n * n ) ^ n - 1

    this can happen n times



    N!?

    Tries everything. N rows to loop through, N columns to try until board is exhausted. Then can backtrack to the start
    and try another N times. Can do 'full backtracks' (from board exhaustion) N times when setting queen in first row,
    N - 1 times for setting queen in 2nd row, N - 2 for setting queen in 3rd row and 1 time in setting the last queen.
    (N * N)^N!

Space Complexity:
- O(n) use 1 board.
"""


"""
Assume the time complexity of this function is T(N - row_index, N), where N is the size of the board.
Let M(N) be the complexity of the can_place_queen

T(N - row_index, N) = (N - row_index) * T(N - (row_index + 1)) + N * M(N)
    in each solve, can_place_queen is called N times.
    If we ignore the diagonal cases (because that's hard to analysis), solve() is called (N - row_index) times.

So solve(0, board_config, n) will call solve(1, board_config, n), N times
each call of solve(1, board_config, n) will call solve(2, board_config, n),  N - 1 times.
etc

So the size of the search tree is N * (N - 1) * ... * 2 * 1 => N!
Each node in the search tree need to call can_place_queen N times
So the total time complexity is O(N! * N * M(N)) => O(N!*(N^2))
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

"""
time complexity: O(N)
when N is the total number of rows, not the n passed to this funtion
because this function loops through each cells in one row, then each cells in one colum,
then each cells in the main and the secondary diagonal.
"""
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

