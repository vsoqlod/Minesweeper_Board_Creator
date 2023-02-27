# Jae Bum Jang
# Fall 2022, 9/7/22
# Minesweeper board creator which user can modify board size in Row * Column between 5 to 10 and illustrate the number of mines around it.

import check_input
import random


def place_mines(board, mines):
    """Generates the random row and column within the bounds of grid pertaining to the user input then place number of mines in a board which also assign by user.
  Args: 
      board (list): list pass from main()
      mines (int): user input from main()
  Returns:
      board that mines placed 
  """
    while mines != 0:
        random_row = random.randint(0, len(board) - 1)
        random_column = random.randint(0, len(board[0]) - 1)
        if (board[random_row][random_column]) != 'X':
            board[random_row][random_column] = 'X'
            mines -= 1
    return board


def count_mines(board):
    """count the eight spots surrounded by "X"(mine) for each grids except "X".
  Args: 
      board(list): list passed from main() """
    # i and j are used to keep track of where we are in the list
    i = 0
    # Nested loop to traverse board list
    for row in board:
        j = 0
        for column in row:
            if column != "X":
                x = i - 1
                # Nested loop to check surrounding list for mines
                for first in range(3):
                    y = j - 1
                    for second in range(3):
                        if x >= 0 and y >= 0 and x <= len(
                                board) - 1 and y <= len(board[0]) - 1:
                            if board[x][y] == "X":
                                board[i][j] += 1
                        y += 1
                    x += 1
            j += 1
        i += 1


def display_board(board):
    """display all contents of the grid by iterating the 2D lists and nested for loops
  Args:
      board(list): list pass from main()
  """
    for row in board:
        for columns in row:
            print(columns, end=' ')  #here
        print()


def main():
    """Prompt user to set the size of the board and number of mines, except the grid with values, fill with zeros and call the functions."""
    board = []
    print("Minesweeper Maker")
    rows = check_input.get_int_range('Enter number of rows within range 5 - 10: ', 5, 10)
    columns = check_input.get_int_range('Enter number of columns within range 5 - 10: ', 5, 10)
    mines = check_input.get_int_range('Enter number of mines within range 5 - 10: ', 5, 10)

    for row_index in range(rows):
        board_row = [0] * columns
        board.append(board_row)

    print()
    place_mines(board, mines)
    count_mines(board)
    display_board(board)


main()
