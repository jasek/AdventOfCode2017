

from timeit import default_timer as timer
start = timer()

register = {}
maxv = 0
with open('Day8_input.txt') as f:
    data = f.read()
    print(data)
for row in data.split('\n'):
    row = row.split()
    reg = row[0]
    op = row[1]
    val = int(row[2])
    creg = row[4]
    cop = row[5]
    cval = int(row[6])
    print(row)
    cond = False
    if (creg not in register):
        register[creg] = 0
    if (reg not in register):
        register[reg] = 0
    if (cop == '=='):
        if (register[creg] == cval):
            cond = True
    elif (cop == '<'):
        if (register[creg] < cval):
            cond = True
    elif (cop == '>'):
        if (register[creg] > cval):
            cond = True
    elif (cop == '<='):
        if (register[creg] <= cval):
            cond = True
    elif (cop == '>='):
        if (register[creg] >= cval):
            cond = True
    elif (cop == '!='):
        if (register[creg] != cval):
            cond = True
    if (cond):
        if (op == 'inc'):
            register[reg] += val
        elif(op == 'dec'):
            register[reg] -= val
        if(register[reg] > maxv):
            maxv = register[reg]
print(register)
print('largest: ',max(register.values()))
print('max: ', maxv)
end = timer()
print("Time elapsed: ",end - start)