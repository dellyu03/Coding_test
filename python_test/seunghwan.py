#체스판 문제
'''
n, m=map(int, input().split())


original=[]

for _ in range(n):
    original.append(input()) 

BChessPan=[['B' for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i%2!=0 and j%2==0:
            BChessPan[i][j]='W' 
        elif i%2==0 and j%2!=0:
            BChessPan[i][j]='W' 

WChessPan=[['W' for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):

        if i%2!=0 and j%2==0: 
            WChessPan[i][j]='B' 
        elif i%2==0 and j%2!=0: 
            WChessPan[i][j]='B'
cntlist=[]


for i in range(n-7): 
    for j in range(m-7): 
        cntB=0 
        cntW=0 
        


        for p in range(8):
            for q in range(8):
                if original[i+p][j+q] !=BChessPan[p][q]:
                    cntB+=1
                if original[i+p][j+q] !=WChessPan[p][q]:
                    cntW+=1

        cntlist.append(cntB)
        cntlist.append(cntW)

print(min(cntlist))

'''

#영화감독 숌
n = int(input())
movieName = 666
sequenceNum = 0

while True:
    if '666' in str(movieName):
        sequenceNum += 1
    if sequenceNum == n:
        print(movieName)
        break
    movieName +=1


