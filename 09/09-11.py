#~/college/python-nfbgu/09/
a = int(input())
white = list()

for i in range(a):
    white.append(input())

b = int(input())
black = list()
res = list()

for i in range(b):
    black.append(input())
    for j in range(a):
        if black[i] in white[j]:
            res.append(black[i])
            
for i in range(len(res)):
    print(res[i])
