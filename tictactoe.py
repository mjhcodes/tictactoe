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
    """checks the requested space on the board; if taken, returns message; if available, places player token at specified coordinates"""
    if self.board[x][y] != " ":
      return "Space already taken. Please try again."
    else:
      self.board[x][y] = token

  def calc_winner(self):
    for x in range(len(self.board)):
      if "X" in self.board[x][0] and "X" in self.board[x][1] and "X" in self.board[x][2]: #checking horizontal from 0,0 to 0,2
        for j in range(len(self.board)):
          if "X" in self.board[j][0] and "X" in self.board[j][1] and "X" in self.board[j][2]: #checking horizontal from 1,0 to 1,2
            for k in range(len(self.board)):
              if "X" in self.board[k][0] and "X" in self.board[k][1] and "X" in self.board[k][2]: #checking horizontal from 2,0 to 2,2
                print("win")
              else:
                print("lost")

      # if "X" in self.board[x][0] and "X" in self.board[x][1] and "X" in self.board[x][2]: #checking horizontal from 0,0 to 0,2

    
            # for k in range(len(self.board)):
            #   if "X" in self.board[k][0] and "X" in self.board[k][1] and "X" in self.board[k][2]:
          

      # print(self.board[x][x]
    # match = 0
    # for x in range(len(self.board)):
    #   # if self.board[x] == self.board[x]:
    #     match = match + 1
    # print(match)

    # match = 0
    # for x in range(3):
    #   if self.board[x][y] == self.board[x][y]:
    #     match = match + 1
    #     if match == 3:
    #       return True
          
  

  def is_full(self):
    """scans each row of the board and returns False, if any section is blank; otherwise, returns True"""
    for row in self.board:
      if any(item == " " for item in row):
        return False
    print("No more moves available. Game over.\n")
    quit()

  def is_game_over(self):
    """runs two methods to determine if game has concluded"""
    return self.calc_winner() or self.is_full()



board = Game()
player_one = Player("Alex", "X")
player_two = Player("Matt", "O")

board.move(0, 0, "X")
board.move(0, 1, "X")
board.move(0, 2, "X")
board.move(1, 0, "X")
board.move(1, 1, "X")
board.move(1, 2, "X")
board.move(2, 0, "X")
board.move(2, 1, "X")
board.move(2, 2, "X")


# board.move(1, 0, "X")
# board.move(0, 2, "Y")

print(board)

board.calc_winner()



