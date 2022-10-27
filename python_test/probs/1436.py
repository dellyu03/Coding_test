#https://www.acmicpc.net/problem/1436

# 영화감독 숌

n = int(input())

sequenceNum = 0
movieName = 666

while True:
    if '666' in str(movieName):
        sequenceNum += 1
    if sequenceNum == n:
        print(movieName)
        break
    movieName += 1