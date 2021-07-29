import sys
from collections import deque


t = int(sys.stdin.readline())

for _ in range(t) :
    n, m = map(int,sys.stdin.readline().split())
    #array = deque()
    array = deque(list(map(int, sys.stdin.readline().split())))
    index = deque(list(range(len(array))))

    index[m] = -1 #타겟을 -1로 설정
    count= 0
    
    while True:
        if array[0] != max(array) :
            array.append(array[0])
            array.popleft()
            index.append(index[0])
            index.popleft()
            
        else :
            count += 1
            if index[0] == -1 :
                print(count)
                break
            else :
                array.popleft()
                index.popleft()
                
            
            
    
    
    
    
    