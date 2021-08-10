import sys

    
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = 0
blue = 1
result = []

def solution(x, y, N) :
    color = arr[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != arr[i][j] :
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == white :
        result.append(0)
    else :
        result.append(1)    

solution(0,0,n)
print(result.count(0))
print(result.count(1))
