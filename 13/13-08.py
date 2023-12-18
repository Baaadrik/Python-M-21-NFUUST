ck = {}

for i in range(int(input())):
    words = input().split()
    word = words[0]
    ck[word] = words[1:len(words) + 1]
    
for i in range(int(input())):
    word = input()
    if word not in ck:
        print('Нет в словаре')
    else:
        print(*ck[word])
