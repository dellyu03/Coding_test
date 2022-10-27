#https://www.acmicpc.net/problem/10828

#my_code
'''
import sys
N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()
    order = input_split[0]
    if order == 'push':
        stack.append(input_split[1])
    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
'''
#수업 예제 코드



import sys
N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()
    order = input_split[0]
    if order == "push":
        stack.append(input_split[1])
    elif order == "pop":
        if (not stack):
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        print(0 if stack else 1)
    elif order == "top":
        print(stack[-1] if stack else -1)

