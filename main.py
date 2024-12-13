import random

class Player:
    def __init__(self,name):
        self.name = name
        self.pick = None


class Game:
    def __init__(self):
        self.grid = [[" "," "," "], [" "," "," "], [" "," "," "]]
        name = input("Enter a name: ")
        self.player = Player(name)
        self.bot = Player("Bot")
        self.turn = [self.player]
        randnum = random.randint(0,1)
        if randnum == 0:
            print(f"You are X, {self.player.name} goes first")
            self.player.pick = "X"
            self.bot.pick = "O"
            self.turn.append(self.bot)
        else:
            print(f"You are O, {self.bot.name} goes first")
            self.player.pick = "O"
            self.bot.pick = "X"
            self.turn.insert(0, self.bot)

    def loopy(self):
        winner = False
        current_player = None
        while winner != True:
            print(f"{self.grid[0]}\n{self.grid[1]}\n{self.grid[2]}")
            match self.turn[0]:
                case self.player:
                    current_player = self.player
                    print(f"{self.player.name}'s turn")
                    position = input("Input a valid position from 1-9: ")
                    # if position.isnumeric():
                    #     position = int(position)
                    #     print(position)
                    # else:
                    #     print("Please input a number between 1-9")


                case self.bot:
                    current_player = self.bot
                    print("Bot's turn")
                    position = str(random.randint(1,9))


                case _:
                    raise ValueError
            if position.isnumeric() and int(position) <= 9 and int(position) >= 1:
                position = int(position)
                print(position)
                row, column = position // 3, position % 3 - 1
                print(row, column)
                self.grid[row][column] = current_player.pick
                self.turn.append(self.turn.pop(0))
            else:
                print("invalid position")
            #
            # if position <= 9 and position >= 1:
            #     self.turn.append(self.turn.pop(0))
            # else:
            #     print("invalid position")


Game().loopy()
