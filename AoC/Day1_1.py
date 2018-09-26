
sum = 0
inp = input("input")
prev = inp[-1:]
print(prev)
for i in inp:
    print(i)
    if (prev == i):
        sum +=int(i)
    prev = i
print(sum)