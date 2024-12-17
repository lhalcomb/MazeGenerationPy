from __future__ import annotations
import math
import heapq
import pygame

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
            # print(f'Neighboring Wall Direction: {wallDirection}, Wall Exists? {cell.walls[wallDirection]} ')
            if not cell.walls[wallDirection]:
                nx, ny = x + dx, y + dy
                # Ensure the neighbor is within bounds
                newCell = self.grid[nx][ny]
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

    def dijkstrasPathStep(self, start: Cell, end: Cell, priority_queue, cellSize: int, window):
        

        if priority_queue:
            current_cost, current = heapq.heappop(priority_queue)
            if current != end:
                for neighbor in self.neighbors(current):
                    # Assuming movement cost of 1 between adjacent cells
                    new_cost = current.cost + 1
                    if new_cost < neighbor.cost:
                        neighbor.cost = new_cost
                        neighbor.parent = current
                        heapq.heappush(priority_queue, (neighbor.cost, neighbor))

            # Backtrack to find the path
            cellCost, nextCurrent = priority_queue[0]
           
            
            # Draw line segment from `current` to `nextCurrent`
            x1, y1 = current.x * cellSize + cellSize // 2, current.y * cellSize + cellSize // 2
            x2, y2 = nextCurrent.x * cellSize + cellSize // 2, nextCurrent.y * cellSize + cellSize // 2
            pygame.draw.line(window, (0, 255, 255), (x1, y1), (x2, y2), 3)

            # Update `current` to the next cell
            current = nextCurrent
    
        
        # Draw the entire path up to this point
        pathCell = current
        while pathCell.parent:
            x1, y1 = pathCell.x * cellSize + cellSize // 2, pathCell.y * cellSize + cellSize // 2
            x2, y2 = pathCell.parent.x * cellSize + cellSize // 2, pathCell.parent.y * cellSize + cellSize // 2
            pygame.draw.line(window, (0, 255, 0), (x1, y1), (x2, y2), 3)
            pathCell = pathCell.parent

        return current, priority_queue
            


    