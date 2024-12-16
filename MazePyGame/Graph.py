from __future__ import annotations
import math
import heapq

from Cell import Cell

class Graph:
    def __init__(self, grid: list): #initializes the graph, which is the 2d grid of cell objects (maze)
        self.grid = grid
    
    def initializeCosts(self): #sets all costs to infinity except for the start node
        for row in self.grid:
            for cell in row:
                cell.cost = math.inf
                cell.parent = None
    
    def neighbors(self, cell: Cell):
        x, y = cell.x, cell.y
        neighbors = []

        # Directions corresponding to walls: top, right, bottom, left
        for wallDirection, (dx, dy) in enumerate(((0, -1), (1, 0), (0, 1), (-1, 0))):
            # Check if the wall in this direction is open
            if not cell.walls[wallDirection]:
                nx, ny = x + dx, y + dy
                # Ensure the neighbor is within bounds
                if 0 <= ny < len(self.grid) and 0 <= nx < len(self.grid[0]):
                    newCell = self.grid[ny][nx]
                    neighbors.append(newCell)
    
        return neighbors
    
    def dijkstrasPath(self, start: Cell, end: Cell):
        self.initializeCosts()
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))
        start.cost = 0
        visited = set()

        while priority_queue:
            current_cost, current = heapq.heappop(priority_queue)

            if current in visited:
                continue
            visited.add(current)

            if current == end:
                break

            for neighbor in self.neighbors(current):
                # Assuming movement cost of 1 between adjacent cells
                new_cost = current.cost + 1
                if new_cost < neighbor.cost:
                    neighbor.cost = new_cost
                    neighbor.parent = current
                    heapq.heappush(priority_queue, (neighbor.cost, neighbor))

        # Backtrack to find the path
        path = []
        current = end
        while current:
            path.append(current)
            current = current.parent
        return path[::-1]  # Return reversed path (from start to end)



    