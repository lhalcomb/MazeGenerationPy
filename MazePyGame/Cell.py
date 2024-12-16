from __future__ import annotations
import math
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.visited = False
        self.walls = [True, True, True, True] #top, right, bottom, left

        self.set = None # for Kruskals, each set is its own set


        #solving the maze 
        self.cost = math.inf
        self.heuristic = 0.0
        self.parent = None
    
    def __lt__(self, other: Cell):
        # Compare cells based on their cost
        return self.cost < other.cost

    def heuristicMan(self, end: Cell):
    #heuristic function for manhattan distance
        return abs(self.x - end.x) + abs(self.y - end.y)
    
    def heuristicEuclidean(self,  end: Cell):
        #heuristic function for euclidean  distance
        return math.sqrt((self.x - end.x)**2 + (self.y - end.y)**2)

