# https://www.acmicpc.net/problem/1021


# 회전하는 큐
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
eraseWanted = list(map(int, input().rstrip().split()))
dq = deque((i+1) for i in range(n))
cnt = 0 
for v in eraseWanted:
    while True:
        if v == dq[0]:
            dq.popleft()
            break
        if dq.index(v) <= len(dq)//2:
            dq.append(dq.popleft())
        else:
            dq.appendleft(dq.pop())
        cnt += 1
print(cnt)
