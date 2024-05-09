"""
There are labels, frames, buttons, etc.
"""

from tkinter import *


class Screen:
    """
    this is the class Screen
    """

    def __init__(self, game):
        # Add Labels, Frames and Button
        self.label = Label(game.root,
                           text="Rock Paper Scissors",
                           font="normal 20 bold",
                           fg="black")
        self.label.pack(pady=20)

        frame_for_label = Frame(game.root)
        frame_for_label.pack()

        self.label_player = Label(frame_for_label,
                                  text="Player			 ",
                                  font=10)
        self.label_vs = Label(frame_for_label,
                              text="VS			 ",
                              font="normal 10 bold")

        self.label_computer = Label(frame_for_label, text="Computer", font=10)

        self.label_player.pack(side=LEFT)
        self.label_vs.pack(side=LEFT)
        self.label_computer.pack()

        self.label_game = Label(game.root,
                                text="",
                                font="normal 20 bold",
                                bg="white",
                                width=15,
                                borderwidth=2,
                                relief="solid")
        self.label_game.pack(pady=20)

        frame_for_button = Frame(game.root)
        frame_for_button.pack()

        self.button_rock = Button(frame_for_button, text="Rock",
                                  font=10, width=7,
                                  command=game.isrock)

        self.button_paper = Button(frame_for_button, text="Paper",
                                   font=10, width=7,
                                   command=game.ispaper)

        self.button_scissors = Button(frame_for_button, text="Scissors",
                                      font=10, width=7,
                                      command=game.isscissors)

        self.button_rock.pack(side=LEFT, padx=10)
        self.button_paper.pack(side=LEFT, padx=10)
        self.button_scissors.pack(padx=10)

        Button(game.root, text="Reset Game",
               font=10, fg="red", command=game.reset_game).pack(pady=20)
