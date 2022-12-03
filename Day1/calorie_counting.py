from collections import deque

with open('listB.txt') as l:
    ls = l.readlines()

total = 0
cals = {}
arr = [0,0,0]
ls.append('\n')

for val in ls:
    val = 0 if val == '\n' else int(val)
    if val == 0:
        i = 0
        for i in range(len(arr)):
            if arr[i] < total:
                arr.insert(i, total)
                arr.pop()
                break
        total = 0
    else: total += val

print(sum(arr))