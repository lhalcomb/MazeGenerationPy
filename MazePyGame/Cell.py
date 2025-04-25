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
    

if __name__ == "__main__":
    # Example usage
    import QLearning
    grid = []
    for x in range(5):
        row = []
        for y in range(5):
            row.append(Cell(x, y))
        grid.append(row)
    for row in grid:
        for cell in row:
            print(f"Cell ({cell.x}, {cell.y}) ")
    
    ql = QLearning.QLearning(grid, grid[0][0], grid[4][4])
    ql.train(500)
    print(ql.get_valid_actions(grid[0][0]))

   

