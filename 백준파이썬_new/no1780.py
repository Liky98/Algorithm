import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = []

def solution(x, y, N) :
    color = arr[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != arr[i][j] :
                solution(x, y, N//3)
                solution(x + N//3, y, N//3)
                solution(x + N//3 *2, y, N//3)
                solution(x + N//3 *2, y + N//3, N//3)
                solution(x, y + N//3, N//3)
                solution(x, y + N//3 * 2, N//3)
                solution(x+N//3, y + N//3 * 2, N//3)
                solution(x+N//3, y+N//3, N//3)
                solution(x+N//3 *2, y+N//3 *2, N//3)
                return
    if color == 0 :
        result.append('0')
    elif color == 1 :
        result.append('1') 
    else :
        result.append('-1')   

solution(0,0,n)
print(result.count('-1'))
print(result.count('0'))
print(result.count('1'))
