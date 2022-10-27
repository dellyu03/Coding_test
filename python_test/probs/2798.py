# https://www.acmicpc.net/problem/2798
# 블랙잭

N, M = map(int, input().split())
numList = list(map(int, input().split()))
sumList=[]

for app in numList[:]:
    for app1 in numList[:]:
        for app2 in numList[:]:
            if app == app1 or app == app2 or app1 == app2:
                continue
            sum = app+app1+app2
            sumList.append(sum)
sumAppList = []
for s in sumList:
    if s<=M:
        sumAppList.append(s)
print(max(sumAppList))