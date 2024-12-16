
from Cell import Cell

grid = []
cell = Cell(0, 0)

for x in range(10):
    row = []
    for y in range(10):
        row.append(Cell(x, y))
    grid.append(row)


grid.reverse()
for row in grid:
    for cell in row:
        print(cell.x, cell.y)


alist = [0,1,2,3,4,5]

print(alist[::-1]) 
alist.reverse()
print(alist)



