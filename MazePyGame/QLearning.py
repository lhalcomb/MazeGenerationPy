
"""Q-learning algorithm for reinforcement learning in a maze environment."""
from __future__ import annotations
import numpy as np
import random
import math
from matplotlib import pyplot as plt
from Cell import Cell



# Q-learning algorithm
"""
Q-learning is a model-free reinforcement learning algorithm used to learn the value of an action in a particular state.

    It is used in various applications, including game play, robotics, and control systems.
The algorithm learns a policy that tells an agent what action to take under what circumstances.
The Q-learning algorithm is based on the Bellman equation, which describes the relationship between the value of a state and the values of its successor states.
The Q-value (or action-value) is a measure of the quality of an action taken in a given state.
The Q-learning algorithm updates the Q-values based on the reward received after taking an action and the maximum expected future rewards. 
"""
class QLearning:
    def __init__(self, grid: list , start: Cell, end: Cell, alpha: float = 0.1, gamma: float = 0.9, epsilon: float = 0.1, epsilon_decay: float = 0.995):
        """
        Initialize the Q-learning algorithm.

        Parameters:
        grid (list of list of Cell): The maze represented as a grid of cells.
        start (Cell): The starting cell.
        end (Cell): The ending cell.
        alpha (float): The learning rate.
        gamma (float): The discount factor.
        epsilon (float): The exploration rate.
        epsilon_decay (float): The decay rate for epsilon.
        """
        self.grid = grid
        self.start = start
        self.end = end
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.actions = [0, 1, 2, 3] # up, right, down, left
        self.q_table = {} #{(x, y): [q_up, q_right, q_down, q_left]}

    def get_valid_actions(self, cell: Cell):
        """
        Get valid actions for a given cell.

        Parameters:
        cell (Cell): The current cell.

        Returns:
        list: A list of valid actions.
        """
        valid_actions = []
        for action in self.actions:
            if cell.walls[action] == False: #top = 0, right = 1, bottom = 2, left = 3
                # Check if the action is valid (i.e., it doesn't lead to a wall)
                valid_actions.append(action)

        return valid_actions
    
    def choose_action(self, state: Cell):
        """
        Choose an action based on the epsilon-greedy policy.
        Parameters:
        state (Cell): The current state.
        Returns:
        int: The chosen action.


        """

        if random.random() < self.epsilon:
            # Explore: choose a random action
            return random.choice(self.get_valid_actions(self.grid[state.x][state.y]))
        else:
            return self.get_best_action(state)
    
    def get_best_action(self, state: Cell):
        """
        Get the best action for a given state based on the Q-table.

        Parameters:
        state (Cell): The current state.

        Returns:
        int: The best action.
        """
        q_values = self.q_table.get((state.x, state.y), [0] * len(self.actions))
        valid_actions = self.get_valid_actions(self.grid[state.x][state.y])
        best_action = max(valid_actions, key=lambda action: q_values[action])

        return best_action
    
    def step(self, state, action):
        """
        Take a step in the environment.

        Parameters:
        state (Cell): The current state.
        action (int): The action to take.

        Returns:
        tuple: The next state and the reward.
        """
        x, y = state.x, state.y

        if action == 0: y -= 1 # up
        elif action == 1: x += 1 # right
        elif action == 2: y += 1 # down
        elif action == 3: x -= 1 # left
        # Ensure the new state is within bounds
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[0]):
            return (state.x, state.y) # Stay in the same state if out of bounds
        
        return (x, y) # Return the new state
    def train(self, episodes: int):
        pass
    

    def train_step_by_step(self, episodes: int):
        pass
    

    