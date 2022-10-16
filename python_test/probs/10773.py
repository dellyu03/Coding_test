# my code
'''
import sys

K = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(K):
    input = int(sys.stdin.readline().rstrip())
    if input == 0:
        stack.pop()
    else:
        stack.append(input)

print(sum(stack))
'''

#수업 예제 코드
'''
import sys

K = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(K):
    input = int(sys.stdin.readline().rstrip())
    if input == 0:
        stack.pop()
        continue
    else:
        stack.append(input)

print(sum(stack))
'''
