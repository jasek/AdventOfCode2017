
from timeit import default_timer as timer

with open('Day6_input.txt') as f:
    data = f.read()
start = timer()
entrystate = [int(n) for n in data.split()]
ram =  [int(n) for n in data.split()]
size = len(ram)
print(entrystate)
steps = 0 
states = []

while ''.join(str(v) for v in ram) not in states:
    states.append(''.join(str(v) for v in ram))
    steps += 1
    biggest = ram.index(max(ram))
    biggestval = ram[biggest]
    ram[biggest] = 0
    for i in range(biggestval):
        ram[(biggest + 1 +i) % size] += 1
    #print(ram, 'sum', sum(ram), entrystate)
    #if (entrystate == ram):
    #    break;


print(steps, steps - states.index(''.join(str(v) for v in ram)))
end = timer()
print("Time elapsed: ",end - start)