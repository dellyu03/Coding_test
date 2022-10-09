from collections import deque
import sys

input = (sys.stdin.readline)
n = int(input())
queue = deque()
for i in range(n):
    queue.append(i+1)

for _ in range(n-1):
    queue.popleft()
    a = queue.popleft()
    queue.append(a)

print(queue[0])
