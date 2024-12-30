
from Cell import Cell
from Queue import MyQueue 

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

queue = MyQueue()
queue.is_empty()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)


queue.print_queue()
queue.dequeue()
queue.print_queue()  # prints 2, 3



