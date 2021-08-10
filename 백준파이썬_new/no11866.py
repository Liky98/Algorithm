import sys 
from collections import deque

array = deque()
n, k = map(int, sys.stdin.readline().split())

for i in range(n) :
    array.append(i+1)
    
print("<", end='')

while array :
    for i in range(k-1) :
        array.append(array[0])
        array.popleft()
    
    print("{}".format(array.popleft()), end='')
    if array :
        print(", ",end='')

print(">")


