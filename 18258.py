#https://www.acmicpc.net/problem/18258
#수업 예제 코드
'''
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
queue = deque()
for  _ in range(N):
    i = sys.stdin.readline().split()
    if i [0] =='push':
        queue.append(int(i[1]))  
    elif i [0] == 'pop':
        if not queue :
            print(-1)
        else:
            print(queue[0])
            queue.popleft()     
    elif i[0] == 'size':
        print(len(queue))
    elif i[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else :
            print(0)
    elif i[0] == 'front':
        if not queue:
            print(-1)
        else :
            print(queue[0])
    elif i[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
'''