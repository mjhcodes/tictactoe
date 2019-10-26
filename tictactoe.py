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

  def calc_winner(self, current_player):
    """checks for a winner, based on horizontal, vertical and diagonal directions"""

    # horizontal
    for row in self.board:
      if all(item == "X" for item in row) or all(item == "O" for item in row):
        print(f"{current_player.token} is the winner! Congrats, {current_player}!\n")
        quit()

    # vertical
    if (self.board[0][0] == self.board[1][0] == self.board[2][0]) and self.board[0][0] != ' ':
      print(f"{current_player.token} is the winner! Congrats, {current_player}!\n")
      quit()
    elif (self.board[0][1] == self.board[1][1] == self.board[2][1]) and self.board[0][1] != ' ':
      print(f"{current_player.token} is the winner! Congrats, {current_player}!\n")
      quit()
    elif (self.board[0][2] == self.board[1][2] == self.board[2][2]) and self.board[0][2] != ' ':
      print(f"{current_player.token} is the winner! Congrats, {current_player}!\n")
      quit()

    # diagonal - top left to bottom right
    if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != ' ':
      print(f"{current_player.token} is the winner! Congrats, {current_player}!\n")
      quit()

    # diagonal - bottom left to top right
    if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[0][2] != ' ':
      print(f"{current_player.token} is the winner! Congrats, {current_player}!\n")
      quit()
      
  def is_full(self):
    """scans each row of the board and returns False, if any section is blank; otherwise, prints message and quits"""
    for row in self.board:
      if any(item == " " for item in row):
        return False
    print("No more moves available. Game over.\n")
    quit()

  def is_game_over(self, current_player):
    """runs two methods to determine if game has concluded"""
    return self.calc_winner(current_player) or self.is_full()


# - - - - - - - END CLASSES - - - - - - - -


def get_current_player(current_round, player_one, player_two):
  """determines who is the current player based on the current round"""
  if current_round % 2 == 0:
    return player_two
  else:
    return player_one

def main():
  board = Game()

  name_one = input("\nPlayer One - You will be 'X': What is your name? ")
  player_one = Player(name_one, "X")

  name_two = input("Player Two - You will be 'O': What is your name? ")
  player_two = Player(name_two, "O")

  print(f"\nOkay, {player_one.name} & {player_two.name}... let's play!")
  print(f"\nHere's the board...\n{board}")

  current_round = 1

  while True:

    # alternates player each time through the loop
    current_player = get_current_player(current_round, player_one, player_two)

    # ensures a number is inputted
    try:
      x = int(input(f"{current_player.name}, select your horizontal location (0-2): "))
      y = int(input(f"{current_player.name}, select your vertical location (0-2): "))
    except ValueError:
      print("\nNot a valid input. Please try again...\n")
      continue

    # ensures inputted number is either 0, 1 or 2
    if 0 <= x <= 2 and 0 <= y <= 2:
      is_taken = board.move(y, x, current_player.token)
      if is_taken == True:
        continue
      print(board)
    else:
      print("\nNot a valid move. Please try again...\n")
      continue

    # checks for either a winner or a full board
    board.is_game_over(current_player)

    current_round += 1


main()

