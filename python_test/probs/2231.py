#https://www.acmicpc.net/problem/2231

#분해합

N = int(input())
Ms = []
for M_app in range(N):
    sumDigi = 0
    for eachDigit in str(M_app):
        sumDigi += int(eachDigit)
    if N == M_app + sumDigi:
        Ms.append(M_app)
print(min(Ms) if len(Ms) > 0 else 0)