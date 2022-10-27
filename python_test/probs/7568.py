# https://www.acmicpc.net/problem/7568

# 덩치
N = int(input())
tupleList = []
for _ in range(N):
    a,b = map(int, input().split())
    tuple = (a,b)
    tupleList.append(tuple)

for i in tupleList:
    rank = 1
    for j in tupleList:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end='')