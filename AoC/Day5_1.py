
from timeit import default_timer as timer

jump = 0
pos = 0
data = ''
with open('Day5_input.txt') as f:
    data = f.read()
start = timer()
data = [int(n) for n in data.split()]

print(data)
while pos < len(data) and pos >= 0:
    val = data[pos]
    data[pos] += 1
    pos += val
    jump +=1
print(jump)
end = timer()
print("Time elapsed: ",end - start)