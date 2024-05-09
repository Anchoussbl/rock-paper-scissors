"""
This is a game logic.
"""

import random
from screen import *


class Game:
    """
    the main class of the game
    """

    def __init__(self):
        self.root = Tk()
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("500x500")
        self.screen = Screen(self)
        self.computer_value = {
            "0": "Rock",
            "1": "Paper",
            "2": "Scissors"
        }
        self.reset_game()

    def run(self):
        """
        Start of the game
        """
        self.root.mainloop()

    def reset_game(self):
        """
        Reset The Game
        """
        self.screen.button_rock["state"] = "active"
        self.screen.button_paper["state"] = "active"
        self.screen.button_scissors["state"] = "active"
        self.screen.label_player.config(text="Player			  ")
        self.screen.label_computer.config(text="Computer")
        self.screen.label_game.config(text="")

    def button_disable(self):
        """
        Disable the Button
        """
        self.screen.button_rock["state"] = "disable"
        self.screen.button_paper["state"] = "disable"
        self.screen.button_scissors["state"] = "disable"

    def isrock(self):
        """
        If player selected rock
        """
        c_v = self.computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Match Draw"
        elif c_v == "Scissors":
            match_result = "You Win"
        else:
            match_result = "Computer Win"
        self.screen.label_game.config(text=match_result)
        self.screen.label_player.config(text="Rock		 ")
        self.screen.label_computer.config(text=c_v)
        self.button_disable()

    def ispaper(self):
        """
        If player selected paper
        """
        c_v = self.computer_value[str(random.randint(0, 2))]
        if c_v == "Paper":
            match_result = "Match Draw"
        elif c_v == "Scissors":
            match_result = "Computer Win"
        else:
            match_result = "You Win"
        self.screen.label_game.config(text=match_result)
        self.screen.label_player.config(text="Paper		 ")
        self.screen.label_computer.config(text=c_v)
        self.button_disable()

    def isscissors(self):
        """
        If player selected scissors
        """
        c_v = self.computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Computer Win"
        elif c_v == "Scissors":
            match_result = "Match Draw"
        else:
            match_result = "You Win"
        self.screen.label_game.config(text=match_result)
        self.screen.label_player.config(text="Scissors		 ")
        self.screen.label_computer.config(text=c_v)
        self.button_disable()
