
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.visited = False
        self.walls = [True, True, True, True] #top, right, bottom, left

        self.set = None # for Kruskals, each set is its own set
    

