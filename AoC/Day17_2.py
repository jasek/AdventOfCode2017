stop = 50000001
zero = 0
inp = 349
pos = 1
for i in range(2,stop):
    newp = pos + (inp % i)
    newp = newp % (i)
    pos = newp + 1
    #print(pos)
    if (pos == 1):
        zero = i
        print(zero)
print(zero)
