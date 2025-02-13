#Game 

import random

class Stonepaper:
    choices = ['rock', 'paper', 'scissor']

    def __init__ (self, rounds):
        self.tround = rounds
        self.cround = 0
        self.userwin = 0
        self.computerwin = 0

    def getComputerChoice(self):
        return random.choice(self.choices)

    def detwinner(self, userchoice, computerchoice):
        if userchoice == computerchoice:
            return "It's a tie!"
        elif (userchoice == 'rock' and computerchoice == 'scissor') or \
             (userchoice == 'scissor' and computerchoice == 'paper') or \
             (userchoice == 'paper' and computerchoice == 'rock'):
            self.userwin += 1
            return "You win this round!"
        else:
            self.computerwin += 1
            return "Computer wins this round!"

    def check_game_winner(self):
        if self.userwin > self.tround // 2:
            return "Jeet Gaye\n"
        elif self.computerwin > self.tround // 2:
            return "Haar Gaye\n"
        return None

    def play(self):
        print("\nSwagat Hai Aapka is Game mai\n")
        
        print(f"Best of {self.tround} rounds. Let's go\n")

        while self.cround < self.tround:
            print(f"Round {self.cround + 1}/{self.tround}")

            userchoice = input("Choose rock, paper, or scissor = ").strip().lower()
            if userchoice not in self.choices:
                print("Invalid choice\n")
                continue

            computerchoice = self.getComputerChoice()
            print(f"Computer chose: {computerchoice}")

            result = self.detwinner(userchoice, computerchoice)
            print(result)
            print(f"Score = You- {self.userwin} & Computer- {self.computerwin}\n")

            self.cround += 1

            game_winner = self.check_game_winner()
            if game_winner:
                print(game_winner)
                break

        print("\nGame Over!! Final Score = \n")
        print(f"You = {self.userwin} & Computer = {self.computerwin}\n")

rounds = int(input("Enter the number of rounds to play = \n"))

game = Stonepaper(rounds)
game.play()