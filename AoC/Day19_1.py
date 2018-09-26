
import string
from timeit import default_timer as timer
start = timer()

maze = []
x = 0
y = 0
direction = 'd'

with open('Day19_input.txt') as f:
    data = f.readlines()
    #print(data)
for row in data:
    row = row.replace('\n','')
    maze.append(row)
print(maze)
x = maze[0].index('|')
print(x)

letters = ''
width = len(maze[0])
heigth =len(maze)
steps = 0

while True:
    steps += 1
    if (direction == 'd'):
        y += 1
    elif (direction == 'u'):
        y -= 1
    elif (direction == 'l'):
        x -= 1
    elif (direction == 'r'):
        x += 1
    s = maze[y][x]
    #print(s)
    print('res', letters, steps)
    if (s in string.ascii_uppercase):
        letters+=s
    elif (s == '+'):
        if (direction == 'd' or direction == 'u'):
            if (x == 0 or maze[y][x-1] == ' '):
                direction = 'r'
            #elif (x+1 == width or maze[y][x+1] == ' '):
            #    break
            else:
                direction = 'l'
        else:
            if (y == 0 or maze[y-1][x] == ' '):
                direction = 'd'
            #elif (y+1 == heigth or maze[y+1][x] == ' '):
                #break
            else:
                direction = 'u'
print('res', letters)


end = timer()
print("Time elapsed: ",end - start)