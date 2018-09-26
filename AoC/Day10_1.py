
from itertools import cycle
from timeit import default_timer as timer
start = timer()

size = 256
skip = 0
pos = 0
with open('Day10_input.txt') as f:
    data = f.read()
data = list(map(int,data.split(',')))
print(data)

lst = list(range(size))
#pool = cycle(lst)

#for item in pool:
#    print(item)
#print(pool[1:3])
print(lst)

for l in data:
    sublist = []
    for i in range(pos, pos + l):
        it = i % size
        sublist.append(lst[it])
    print(sublist)
    sublist = sublist[::-1]
    print(sublist)
    for i in range(len(sublist)):
        it = (i + pos) % size
        lst[it] = sublist[i]


    print('lst',lst)

    pos += l
    pos += skip
    pos = pos % size
    skip += 1


res = lst[0] * lst[1]
print('res', res)

end = timer()
print("Time elapsed: ",end - start)

