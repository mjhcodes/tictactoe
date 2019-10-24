import random

class Player:
  def __init__(self, name, token):
    self.name = name
    self.token = token

  def __repr__(self):
    return self.token

class Game:
  def __init__(self, board):
    self.board = board

  def __repr__(self):
    pass

  def move(self, x, y, player):
    """checks the requested space on the board; if taken, returns message; if available, places player token at specified coordinates"""
    if self.board[x][y] != ' ':
      return 'Space already taken. Please try again.'
    else:
      self.board[x][y] = player

  def calc_winner(self):
    pass

  def is_full(self):
    pass

  def is_game_over(self):
    """runs two methods to determine if game has concluded"""
    return self.calc_winner() or self.is_full()

import random

#building the board:

width = 3 # the width of the board
height = 3  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ' + "|")  # append an empty space to the board


for i in range(height):
    for j in range(width):
      print(board[i][j], end=' ')  # printing the board
    print()
