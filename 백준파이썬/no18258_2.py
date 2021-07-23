def push(num) :
    list.append(num)

def pop() :
    if len(list) != 0 :
       print(list.popleft())
    else :
        print(-1)
def size() :
    print(len(list))

def empty() :
    if len(list) != 0 :
        print(0)
    else :
        print(1)

def front() :
    if len(list) != 0 :
        print(list[0])
    else : print(-1)

def back() :
    if len(list) != 0 :
        print(list[-1])
    else :
        print(-1)

import sys 
from collections import deque

list = deque([])
for i in range(int(sys.stdin.readline())) :
    x = sys.stdin.readline().split()
    if x[0] == 'push' :
        push(x[1])
    elif x[0] =='pop' :
        pop()
    elif x[0] == 'size' :
        size()
    elif x[0] == 'empty' :
        empty()
    elif x[0] == 'front' :
        front()
    else :
        back()