import sys

n = int(sys.stdin.readline())
arr = [list(map(int, input())) for _ in range(n)]

white = 1

result = []

def solution(x, y, N) :
    color = arr[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != arr[i][j] :
                print("(", end="")
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                print(")",end='')
                return
    if color == white :
        print(1, end='')
    else :
        print(0, end='')
        
solution(0,0,n)