import numpy as np
import pandas as pd


class RockPaperScissors:

    def __init__(self):
        # Agent is the first index, opponent is the second index
        # Rock = 0, Paper = 1, Scissors = 2
        self.state = [0, 0]
        self.action_space = [0, 1, 2]
        self.win = False
        self.lose = False
        self.tie = False
        self.state_dict = {(0, 0): 0,
                           (0, 1): 1,
                           (0, 2): 2,
                           (1, 0): 3,
                           (1, 1): 4,
                           (1, 2): 5,
                           (2, 0): 6,
                           (2, 1): 7,
                           (2, 2): 8}

    def reset(self):
        self.state = [0, 0]
        self.action_space = [0, 1, 2]
        self.win = False
        self.lose = False
        self.tie = False

    def update_state(self, agent_move, opponent_move):
        self.state = [agent_move, opponent_move]

    def game_over(self):
        # Determines win / lose / tie
        if self.state_dict[self.state] == 0 or self.state_dict[self.state] == 4 or self.state_dict[self.state] == 8:
            self.tie = True
        elif self.state_dict[self.state] == 1 or self.state_dict[self.state] == 5 or self.state_dict[self.state] == 6:
            self.lose = True
        else:
            self.win = True

    def rewards(self):
        reward = 0
        if self.win:
            reward = 1
        elif self.lose:
            reward = -1
        return reward
    



