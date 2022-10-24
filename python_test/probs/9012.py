# #my code
# import sys
# T = int(sys.stdin.readline().rstrip())
# stack = []

# for _ in range(T):
#     input = list(input().rstrip())


# 교수님 코드
def solve(parens):
    stack = []
    
    for paren in parens:
        if len(stack) != 0:
            if paren == ')':
                stack.pop()
                continue
        elif len(stack) == 0:
            if paren == ')':
                print('NO')
                return
        stack.append(paren)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

T = int(input())

for _ in range(T):
    parens = list(input().rstrip())
    solve(parens)