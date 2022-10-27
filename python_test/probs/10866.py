# https://www.acmicpc.net/problem/10866

#덱 문제
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
dq = deque()
for _ in range(n):
    i = sys.stdin.readline().split()
    if i[0] == 'push_front':
        dq.appendleft(int(i[1]))
    elif i[0] == 'push_back':
        dq.append(int(i[1]))
    elif i[0] == 'pop_front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif i[0] == 'pop_back':
        if not dq:
            print(-1)
        else :
            print(dq[-1])
            dq.pop()
    elif i[0] == 'size':
        print(len(dq))
    elif i[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else :
            print(0)
    elif i[0] == 'front':
        if not dq:
            print(-1)
        else :
            print(dq[0])
    elif i[0] == 'back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])