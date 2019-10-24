# Tic Tac Toe great!

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


