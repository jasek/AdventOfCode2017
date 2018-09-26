
from timeit import default_timer as timer

sum = 0
inp = input("Enter input: ")
start = timer()
lenght = len(inp)
half = int(lenght / 2)
for i in range(lenght):
    nextn = i + half
    if (nextn >= lenght):
        nextn = nextn - lenght
    if (inp[i] == inp[nextn]):
        sum +=int(inp[i])
print(sum)

end = timer()
print("Time elapsed: ",end - start)