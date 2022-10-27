# https://www.acmicpc.net/problem/11866

#수업 코드
from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
queue = deque()
for i in range(n):
    queue.append(i+1)
print("<", end = '')
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
print(">")

