# https://www.acmicpc.net/problem/1018

#체스판 다시 칠하기
N, M = map(int, input().split())

original = []
for _ in range(N):
    original.append(input())
BChessPan = [['B' for _ in range(8)] for _  in range(8)]
for i in range(8):
    for j in range(8):
        if i%2 !=0 and j%2 == 0:
            BChessPan[i][j] = 'W'
        elif i % 2 == 0 and j % 2 != 0:
            BChessPan[i][j] = 'W'

WChessPan = [['W' for _ in range(8)] for _  in range(8)]
for i in range(8):
    for j in range(8):
        if i%2 !=0 and j%2 == 0:
            WChessPan[i][j] = 'B'
        elif i % 2 == 0 and j % 2 != 0:
            WChessPan[i][j] = 'B'

cntList = []

for i in range(N-7):
    for j in range(M-7):
        cntB = 0
        cntW = 0

        for p in range(8):
            for q in range(8):
                if original[i+p][j+q] != BChessPan[p][q]:
                    cntB+= 1
                if original[i+p][j+q] != WChessPan[p][q]:
                    cntW += 1
        cntList.append(cntB)
        cntList.append(cntW)
print(min(cntList))
