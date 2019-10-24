class Player:
  def __init__(self, name, token):
    self.name = name
    self.token = token

  def __repr__(self):
    return self.token

class Game:
  def __init__(self):
    self.board = [[' ' for x in range(3)] for y in range(3)]

  def __repr__(self):
    display = "\n"
    for row in self.board:
      display += "|".join(row)
      display += "\n"
    return display

  def move(self, x, y, token):
    """checks the requested space on the board; if taken, returns message; if available, places player token at specified coordinates"""
    if self.board[x][y] != ' ':
      return 'Space already taken. Please try again.'
    else:
      self.board[x][y] = token

  def calc_winner(self):
    pass

  def is_full(self):
    """scans each row of the board and returns False, if any section is blank; otherwise, returns True"""
    for row in self.board:
      if any(item == ' ' for item in row):
        return False
    return True

  def is_game_over(self):
    """runs two methods to determine if game has concluded"""
    return self.calc_winner() or self.is_full()


board = Game()
print(board)
