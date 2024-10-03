import tkinter as tk
import random 
from dataclasses import dataclass, field

root = tk.Tk()
root.title("Maze Generator")
width = 450
height = 450
padding = 20

canvas = tk.Canvas(root, width= width, height = height)
canvas.pack()


@dataclass
class Cell:
    x: int
    y: int
    wall: list = field(default_factory = lambda: [True, True, True, True])
    visited: bool = False

rowCellsCount = 20
colCellsCount = 20
cellSize = 20

grid: list[list[Cell]] = []

def renderCell(cell: Cell, cellSize: int, padding: int):
    xPos = padding + cell.x * cellSize
    yPos = padding + cell.y * cellSize

    top = cell.wall[0]
    right = cell.wall[1]
    bottom = cell.wall[2]
    left = cell.wall[3]

    if top: 
        canvas.create_line(xPos, yPos, xPos + cellSize, yPos, fill = "black")
    if right:
        canvas.create_line(xPos + cellSize, yPos, xPos + cellSize, yPos + cellSize, fill = "black")
    if bottom:
        canvas.create_line(xPos, yPos + cellSize, xPos + cellSize, yPos + cellSize, fill = "black")
    if left:
        canvas.create_line(xPos, yPos, xPos, yPos + cellSize, fill = "black")

    if cell.visited:
        canvas.create_rectangle(xPos, yPos, yPos + cellSize, yPos + cellSize, fill='#888888', outline='')

        


for j in range(colCellsCount):
    row: list[Cell] = []
    for i in range(rowCellsCount):
        row.append(Cell(i, j))
    grid.append(row)




def checkNeighbors(grid: list[list[Cell]], x: int,  y: int):
    
    unvisitedNeighbors = []


    if y > 0 and not grid[y - 1][x].visited:  # Top
        unvisitedNeighbors.append(grid[y - 1][x])
    if x < colCellsCount - 1 and not grid[y][x + 1].visited:  # Right
        unvisitedNeighbors.append(grid[y][x + 1])
    if y < rowCellsCount - 1 and not grid[y + 1][x].visited:  # Bottom
        unvisitedNeighbors.append(grid[y + 1][x])
    if x > 0 and not grid[y][x - 1].visited:  # Left
        unvisitedNeighbors.append(grid[y][x - 1])

       

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
        renderCell(cell, cellSize, padding)

root.update()
input()
