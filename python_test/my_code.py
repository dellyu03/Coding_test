N = int(input())

Doom = []


while len(Doom) != N:
    i = 666
    number = str(i)
    for s in range(len(number)-2):
        tripleNum = number[s:s+3]
        tripleNum = int(tripleNum)
    if tripleNum == 666:
        Doom.append(tripleNum)
    i += 1 

print(Doom)