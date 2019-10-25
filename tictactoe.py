class Player:
  def __init__(self, name, token):
    self.name = name
    self.token = token

  def __repr__(self):
    return self.name

class Game:
  def __init__(self):
    self.board = [[" " for x in range(3)] for y in range(3)]

  def __repr__(self):
    display = "\n"
    for row in self.board:
      display += "|".join(row)
      display += "\n"
    return display

  def move(self, x, y, token):
    """checks the requested space on the board; if taken, prints message and returns True; if available, places player token at specified coordinates"""
    if self.board[x][y] != " ":
      print("\nSpace already taken. Please try again...\n")
      return True
    else:
      self.board[x][y] = token

  def calc_winner(self):
    for x in range(len(self.board)):
      if "X" in self.board[x][0] and "X" in self.board[x][1] and "X" in self.board[x][2] or "X" in self.board[0][x] and "X" in self.board[1][x] and "X" in self.board[2][x]:
        for j in range(len(self.board)):
          if "X" in self.board[j][0] and "X" in self.board[j][1] and "X" in self.board[j][2]: #checking horizontal from 1,0 to 1
            return("win")
          else:
            return("no")
            
        #     for k in range(len(self.board)):
        #       if "X" in self.board[k][0] and "X" in self.board[k][1] and "X" in self.board[k][2] or "X" in self.board[0][k] and "X" in self.board[1][k] and "X" in self.board[2][k]: #checking horizontal from 2,0 to 2,
              




      
  def is_full(self):
    """scans each row of the board and returns False, if any section is blank; otherwise, prints message and quits"""
    for row in self.board:
      if any(item == " " for item in row):
        return False
    print("No more moves available. Game over.\n")
    quit()

  def is_game_over(self):
    """runs two methods to determine if game has concluded"""
    return self.calc_winner() or self.is_full()


# - - - - - - - END CLASSES - - - - - - - -


def get_current_player(current_round, player_one, player_two):
  """determines who is the current player based on the current round"""
  if current_round % 2 == 0:
    return player_two
  else:
    return player_one

board = Game()
player_one = Player("Alex", "X")
player_two = Player("Matt", "O")

board.move(1, 0, "X")
board.move(1, 1, "X")
board.move(1, 2, "X")
# board.move(0, 2, "X")
# board.move(1, 0, "X")
# board.move(1, 1, "X")
# board.move(1, 2, "X")
# board.move(2, 0, "X")
# board.move(2, 1, "X")
# board.move(2, 2, "X")


# board.move(1, 0, "X")
# board.move(0, 2, "Y")

print(board)
print(board.calc_winner())

  # current_round = 1

  # while True:

  #   board.is_game_over()

  #   current_player = get_current_player(current_round, player_one, player_two)

  #   try:
  #     x = int(input(f"{current_player.name}, select your horizontal location (0-2): "))
  #     y = int(input(f"{current_player.name}, select your vertical location (0-2): "))
  #   except ValueError:
  #     print("\nNot a valid input. Please try again...\n")
  #     continue

  #   if 0 <= x <= 2 and 0 <= y <= 2:
  #     is_taken = board.move(y, x, current_player.token)
  #     if is_taken == True:
  #       continue
  #     print(board)
  #   else:
  #     print("\nNot a valid move. Please try again...\n")
  #     continue

  #   current_round += 1


