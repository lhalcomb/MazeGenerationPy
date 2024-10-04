import tkinter as tk
import random 
from dataclasses import dataclass, field

root = tk.Tk()
root.title("Maze Generator")
width = 400
height = 400


canvas = tk.Canvas(root, width= width, height = height)
canvas.pack()


@dataclass
class Cell:
    x: int
    y: int
   # wall: list = field(default_factory = lambda: [True, True, True, True])
    top: bool
    right: bool
    bottom: bool
    left: bool
    visited: bool


rowCellsCount = 15
colCellsCount = 15
cellSize = 20

grid: list[list[Cell]] = []

def renderCell(cell: Cell, cellSize: int):
    xPos = cell.x * cellSize
    yPos = cell.y * cellSize

    top = cell.top
    right = cell.right
    bottom = cell.bottom
    left = cell.left

    
    if cell.visited:
        canvas.create_rectangle(xPos, yPos, xPos + cellSize, yPos + cellSize, fill='#800020', outline='')
        #canvas.create_rectangle(xPos, yPos, yPos + cellSize, yPos + cellSize, fill='#888888', outline='') #makes weird triangular-like rendering 


    if top: 
        canvas.create_line(xPos, yPos, xPos + cellSize, yPos, fill = "black")
    if right:
        canvas.create_line(xPos + cellSize, yPos, xPos + cellSize, yPos + cellSize, fill = "black")
    if bottom:
        canvas.create_line(xPos, yPos + cellSize, xPos + cellSize, yPos + cellSize, fill = "black")
    if left:
        canvas.create_line(xPos, yPos, xPos, yPos + cellSize, fill = "black")


        


for x in range(colCellsCount):
    row: list[Cell] = []
    for y in range(rowCellsCount):
        row.append(Cell(x, y, True, True, True, True, False))
    grid.append(row)




def checkNeighbors(grid: list[list[Cell]], x: int,  y: int):
    
    unvisitedNeighbors = []


    if y > 0 and not grid[x][y - 1].visited:  # Top
        unvisitedNeighbors.append(grid[x][y - 1])
    if x < colCellsCount - 1 and not grid[x + 1][y].visited:  # Right
        unvisitedNeighbors.append(grid[x + 1][y])
    if y < rowCellsCount - 1 and not grid[x][y + 1].visited:  # Bottom
        unvisitedNeighbors.append(grid[x][y + 1])
    if x > 0 and not grid[x - 1][y].visited:  # Left
        unvisitedNeighbors.append(grid[x - 1][y])

       

    return unvisitedNeighbors


    


stack: list[Cell] = [grid[0][0]]



while len(stack):
    current = stack[-1]
    current.visited = True
    stack.pop()
    


    unvisitedNeighbors = checkNeighbors(grid, current.x, current.y)
    

    if unvisitedNeighbors:
        stack.append(current)
        next_cell = random.choice(unvisitedNeighbors)
        stack.append(next_cell)

        if current.x < next_cell.x:
            current.right = False
            next_cell.left = False
        if current.x  > next_cell.x:
            current.left = False
            next_cell.right = False
        if current.y < next_cell.y:
            current.bottom = False
            next_cell.top = False
        if current.y > next_cell.y:
            current.top = False
            next_cell.bottom = False
        next_cell.visited = True
    

 
    
    for row in grid:
        for cell in row:
            renderCell(cell, cellSize)


    root.update()


input()
