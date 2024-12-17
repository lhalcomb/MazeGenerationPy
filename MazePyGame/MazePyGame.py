from queue import Queue
from Cell import Cell
from DisJointSet import DisjointSet
from Graph import Graph

import pygame
import random
import heapq

pygame.init()

width, height = 900, 900

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Generator in PyGame!!")
clock = pygame.time.Clock()
running = True

cell = Cell(0, 0)
grid = []

burgundy = (128, 0, 32)
black = (0, 0, 0)

rowCellsCount = 30
columnCellsCount = 30
cellSize = 30

def renderCell(cell: Cell, cellSize: int):
    xPos = cell.x * cellSize
    yPos = cell.y * cellSize

    top = cell.walls[0]
    right = cell.walls[1]
    bottom = cell.walls[2]
    left = cell.walls[3]

    if cell.visited:
       pygame.draw.rect(window, burgundy, (xPos, yPos, cellSize, cellSize))

    if top: 
        pygame.draw.line(window, black, (xPos, yPos), (xPos + cellSize, yPos), 3)
    if right:
        pygame.draw.line(window, black, (xPos + cellSize, yPos), (xPos + cellSize, yPos + cellSize), 3)
    if bottom:
        pygame.draw.line(window, black, (xPos, yPos + cellSize), (xPos + cellSize, yPos + cellSize), 3)
    if left:
        pygame.draw.line(window, black, (xPos, yPos), (xPos, yPos + cellSize), 3)

def generateGridofCells(columnCellsCount, rowCellsCount):
    for x in range(columnCellsCount):
        row = []
        for y in range(rowCellsCount):
            row.append(Cell(x, y))
        grid.append(row)

def genListofWalls(columnCellsCount, rowCellsCount):
    walls = []

    for x in range(columnCellsCount):
        for y in range(rowCellsCount):
            if x < columnCellsCount - 1: #Right wall
                walls.append(((x,y), (x + 1, y)))
            if y < rowCellsCount - 1: #Bottom Wall
                walls.append(((x,y), (x, y + 1)))
    random.shuffle(walls) # randomize the order of the walls
    
    return walls


def checkNeighbors(grid: list[list[Cell]], x: int,  y: int):

    unvisitedNeighbors = []

    if y > 0 and not grid[x][y - 1].visited:  # Top
        unvisitedNeighbors.append(grid[x][y - 1])
    if x < columnCellsCount - 1 and not grid[x + 1][y].visited:  # Right
        unvisitedNeighbors.append(grid[x + 1][y])
    if y < rowCellsCount - 1 and not grid[x][y + 1].visited:  # Bottom
        unvisitedNeighbors.append(grid[x][y + 1])
    if x > 0 and not grid[x - 1][y].visited:  # Left
        unvisitedNeighbors.append(grid[x - 1][y])

    return unvisitedNeighbors

def DFS_step(stack):
    if len(stack):
        current = stack.pop()
        current.visited = True

        #pygame.draw.rect(window, (255, 215, 0, 3), (xPos, yPos, cellSize, cellSize))
        
        unvisitedNeighbors = checkNeighbors(grid, current.x, current.y)

        if unvisitedNeighbors:
            stack.append(current)
            next_cell = random.choice(unvisitedNeighbors)
            if current.visited:
                pygame.draw.rect(window, (255, 215, 0, 3), (xPos, yPos, cellSize, cellSize))
            stack.append(next_cell)

            if current.x < next_cell.x:
                current.walls[1] = False
                next_cell.walls[3] = False
            if current.x  > next_cell.x:
                current.walls[3] = False
                next_cell.walls[1] = False
            if current.y < next_cell.y:
                current.walls[2] = False
                next_cell.walls[0] = False
            if current.y > next_cell.y:
                current.walls[0] = False
                next_cell.walls[2] = False
            next_cell.visited = True


def DFS_Generate(stack):
    while len(stack):
        current = stack.pop()
        current.visited = True

        #pygame.draw.rect(window, (255, 215, 0, 3), (xPos, yPos, cellSize, cellSize))
        
        unvisitedNeighbors = checkNeighbors(grid, current.x, current.y)

        if unvisitedNeighbors:
            stack.append(current)
            next_cell = random.choice(unvisitedNeighbors)
            if current.visited:
                pygame.draw.rect(window, (255, 215, 0, 3), (xPos, yPos, cellSize, cellSize))
            stack.append(next_cell)

            if current.x < next_cell.x:
                current.walls[1] = False
                next_cell.walls[3] = False
            if current.x  > next_cell.x:
                current.walls[3] = False
                next_cell.walls[1] = False
            if current.y < next_cell.y:
                current.walls[2] = False
                next_cell.walls[0] = False
            if current.y > next_cell.y:
                current.walls[0] = False
                next_cell.walls[2] = False
            next_cell.visited = True

def BFS_step():
    
    if not queue.empty():
        current = queue.get()
        current.visited = True

    
        unvisitedNeighbors = checkNeighbors(grid, current.x, current.y)
    
        if unvisitedNeighbors:

            random.shuffle(unvisitedNeighbors)
            for next_cell in unvisitedNeighbors:
                if not next_cell.visited:
                    if current.x < next_cell.x:
                        current.walls[1] = False
                        next_cell.walls[3] = False
                    if current.x  > next_cell.x:
                        current.walls[3] = False
                        next_cell.walls[1] = False
                    if current.y < next_cell.y:
                        current.walls[2] = False
                        next_cell.walls[0] = False
                    if current.y > next_cell.y:
                        current.walls[0] = False
                        next_cell.walls[2] = False
                
                    next_cell.visited = True
                    queue.put(next_cell)
        

def iterativeRandomized_Kruskals(disjoint_set, walls):
    

    while walls:
        (cell1_pos, cell2_pos) = walls.pop()
        
        x1, y1 = cell1_pos
        x2, y2 = cell2_pos

        cell1 = grid[x1][y1]
        cell2 = grid[x2][y2]

        index1 = y1 * columnCellsCount + x1
        index2 = y2 * columnCellsCount + x2

        # Check if the two cells are in different sets
        if disjoint_set.find(index1) != disjoint_set.find(index2):
            # If they are in different sets, remove the wall between them
            if x1 < x2:  # Right wall
                cell1.walls[1] = False
                cell2.walls[3] = False
            elif x1 > x2:  # Left wall
                cell1.walls[3] = False
                cell2.walls[1] = False
            elif y1 < y2:  # Bottom wall
                cell1.walls[2] = False
                cell2.walls[0] = False
            elif y1 > y2:  # Top wall
                cell1.walls[0] = False
                cell2.walls[2] = False

            # Union the sets of the two cells
            disjoint_set.union(index1, index2)
def iterativeRandomized_Kruskals_step(disjoint_set, walls):
    #comments are for first iteration
    if walls:
        (cell1_pos, cell2_pos) = walls.pop() #pops off random cell tuple of tuples eg. ((18, 6), (18, 7))
        x1, y1 = cell1_pos #sets x1 = 18, y1 = 6
        x2, y2 = cell2_pos #sets x2 = 18, y2 = 7

        cell1 = grid[x1][y1] #cell1 = grid[18][6]
        cell2 = grid[x2][y2] #cell2 = grid[18][7]

        index1 = y1 * columnCellsCount + x1 #index1 = 6 * 20 + 18 = 138
        index2 = y2 * columnCellsCount + x2 #index2 = 7 * 20 + 18 = 158
        
        """ 
        #Debugging

        joinedWalls = []
        if disjoint_set.find(index1) == disjoint_set.find(index2):
            print(f'Set at index one: {disjoint_set.find(index1)}, Set at index two: {disjoint_set.find(index2)}')
            joinedWalls.append((cell1_pos, cell2_pos))
            print(f'First Cell: {joinedWalls[0][0]}, Second Cell: {joinedWalls[0][1]}') """
           
        # Check if the two cells are in different sets

            # If they are in different sets, remove the wall between them
        if disjoint_set.find(index1) != disjoint_set.find(index2):
            if x1 < x2:  # Right wall
                cell1.walls[1] = False
                cell2.walls[3] = False
            elif x1 > x2:  # Left wall
                cell1.walls[3] = False
                cell2.walls[1] = False
            elif y1 < y2:  # Bottom wall
                cell1.walls[2] = False
                cell2.walls[0] = False
            elif y1 > y2:  # Top wall
                cell1.walls[0] = False
                cell2.walls[2] = False

                # Union the sets of the two cells
            disjoint_set.union(index1, index2) #joins the sets and returns to top

def aStar(start: Cell, end: Cell):
    start.heuristic = start.heuristicMan(end)
    start.cost = 0
    openPath = []
    openPath.append(start)

    current = start

    while current != end:
        for wallDirection, item in enumerate(((0, -1), (1, 0), (0, 1), (-1, 0))): #  wall[0] (0, -1), wall[1] (1, 0), wall[2] (0, 1), wall[3] (-1, 0)
            if not current.walls[wallDirection]:
                nextCell = grid[current.x + item[0]][current.y + item[1]]

                if nextCell.cost > current.cost + 1:
                    nextCell.heuristic = nextCell.heuristicMan(end)
                    nextCell.cost = current.cost + 1
                    nextCell.parent = current

                    if nextCell not in openPath:
                        openPath.append(nextCell)

        openPath.remove(current)
        openPath.sort(key=lambda cell: cell.heuristic + cell.cost)
        current = openPath[0]
    
    finalPath = [current]

    while current.parent is not None:
        current = current.parent
        finalPath.insert(0, current)

    return  finalPath

def aStarStep(current: Cell, end: Cell, openPath: list):
    if current != end:
        for wallDirection, item in enumerate(((0, -1), (1, 0), (0, 1), (-1, 0))):
            #print(f'Neighboring Wall Direction: {wallDirection}, Wall Exists? {current.walls[wallDirection]} ')
            if not current.walls[wallDirection]:
                nextCell = grid[current.x + item[0]][current.y + item[1]]
                if nextCell.cost > current.cost + 1:
                    nextCell.heuristic = nextCell.heuristicMan(end)
                    nextCell.cost = current.cost + 1
                    nextCell.parent = current
                    
                    if nextCell not in openPath:
                        openPath.append(nextCell)
        
        if current in openPath:
            openPath.remove(current)

        openPath.sort(key=lambda cell: cell.heuristic + cell.cost)

        if openPath:
            nextCurrent = openPath[0]
            # Update `current` to the next cell
            current = nextCurrent
        
        # Draw the entire path up to this point
        pathCell = current
        while pathCell.parent:
            x1, y1 = pathCell.x * cellSize + cellSize // 2, pathCell.y * cellSize + cellSize // 2
            x2, y2 = pathCell.parent.x * cellSize + cellSize // 2, pathCell.parent.y * cellSize + cellSize // 2
            pygame.draw.line(window, (0, 255, 0), (x1, y1), (x2, y2), 3)
            pathCell = pathCell.parent

    return current, openPath

def generateAStar(current: Cell, end: Cell):

    if current == end:
        pathCell = current
        while pathCell.parent:
            x1, y1 = pathCell.x * cellSize + cellSize // 2, pathCell.y * cellSize + cellSize // 2
            x2, y2 = pathCell.parent.x * cellSize + cellSize // 2, pathCell.parent.y * cellSize + cellSize // 2
            pygame.draw.line(window, (0, 255, 0), (x1, y1), (x2, y2), 3)
            pathCell = pathCell.parent

        
generateGridofCells(columnCellsCount, rowCellsCount)
stack = [grid[0][0]]

queue = Queue()
current = grid[0][0]

queue.put(current)


walls = genListofWalls(columnCellsCount, rowCellsCount)
disjoint_set = DisjointSet(columnCellsCount * rowCellsCount)



xPos = current.x * cellSize
yPos = current.y * cellSize 

DFS_Generate(stack)
#iterativeRandomized_Kruskals(disjoint_set, walls)

graph = Graph(grid)
start = grid[0][0]
end = grid[columnCellsCount - 1][rowCellsCount - 1] 
graph.initializeCosts()
priority_queue = []
heapq.heappush(priority_queue, (0, start))
start.cost = 0
# openPath = []
current = start
# start.heuristic = start.heuristicMan(end)
# start.cost = 0
# openPath.append(start)
# finalPath = aStar(start, end)

pathSearch = True #dijkstra's step logic

while running:
    #for stepping through a*
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        
    window.fill("gray")


    #DFS_step(stack)
    #DFS_Generate(stack)
    #BFS_step()
    #iterativeRandomized_Kruskals(disjoint_set, walls)
    #iterativeRandomized_Kruskals_step(disjoint_set, walls)  
    for row in grid:
        for cell in row:
            renderCell(cell, cellSize)
    
    
    # current, openPath = aStarStep(current, end, openPath)
    # generateAStar(current, end)
    
    # openPath = graph.dijkstrasPath(start, end)
    # for cell in openPath:
    #     if cell.parent:
    #         pygame.draw.line(
    #         window, 
    #         (255, 255, 0), 
    #         (cell.x * cellSize + cellSize // 2, cell.y * cellSize + cellSize // 2), 
    #         (cell.parent.x * cellSize + cellSize // 2, cell.parent.y * cellSize + cellSize // 2), 
    #         2
    #     )
    
    priority_queue = graph.dijkstrasPathStep(current, end, priority_queue, cellSize, window)
    print(priority_queue)
    

    
    # for cell in finalPath[1:]:
    #     pygame.draw.line(window, 
                        # (255, 255, 0), 
                        # (cell.x * cellSize + cellSize//2, cell.y * cellSize + cellSize//2), 
                        # (cell.parent.x * cellSize +  cellSize//2, cell.parent.y * cellSize + cellSize//2), 
                        # 2)
    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
