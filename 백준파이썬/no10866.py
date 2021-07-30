import sys
import collections

T = int(sys.stdin.readline())
array = collections.deque([])

for _ in range(T) :
    x = sys.stdin.readline().split()
    if x[0] == "push_front" :
        array.append(x[1])
    elif x[0] == "push_back" :
        array.appendleft(x[1])
    elif x[0] == "pop_front" :
        if len(array) != 0 :
            print(array.pop())
        else :
            print(-1)
    elif x[0] == "pop_back" :
        if len(array) != 0 :
            print(array.popleft())
        else :
            print(-1)
    elif x[0] == "size" :
        print(len(array))
    elif x[0] == "empty" :
        if len(array) != 0 :
            print(0)
        else :
            print(1)
    elif x[0] == "front" :
        if len(array) != 0 :
            print(array[-1])
        else:
            print(-1)
    else :
        if len(array) != 0 :
            print(array[0])     
        else :
            print(-1)