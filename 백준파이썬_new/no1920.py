import sys
import collections 
_ = int(sys.stdin.readline())
N = set(sys.stdin.readline().split())
_ = int(sys.stdin.readline())
M = sys.stdin.readline().split()



for i in M :
    sys.stdout.write('1\n') if i in N else sys.stdout.write('0\n')