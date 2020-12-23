import numpy as np
import pandas as pd

class RockPaperScissors():

    def __init__(self):
        # Agent is the first index, enemy is the second index
        # Rock = 1, Paper = 2, Scissors = 3
        self.state = [0,0]
        self.action_space = [1,2,3]
        self.win = false
        self.lose = false
        self.tie = false

    def reset(self):
        self.state = [0, 0]
        self.action_space = [1, 2, 3]
        self.win = false
        self.lose = false
        self.tie = false

    def game_over(self):
        #Determines win / lose / tie
        if self.state[0] == 1:
            if self.state[1] == 1:
                self.tie = true
            if self.state[1] == 2:
                self.lose = true
            if self.state[1] == 3:
                self.win = true
        if self.state[0] == 2:
            if self.state[1] == 1:
                self.win = true
            if self.state[1] == 2:
                self.tie = true
            if self.state[1] == 3:
                self.lose = true
        if self.state[0] == 3:
            if self.state[1] == 1:
                self.lose = true
            if self.state[1] == 2:
                self.win = true
            if self.state[1] == 3:
                self.tie = true

    def rewards(self):
        reward = 0
        if self.win == true:
            reward = 1
        elif self.lose == true:
            reward = -1
    



