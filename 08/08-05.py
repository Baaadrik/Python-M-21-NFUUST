#/college/python-nfbgu/08/
res = ''
number = int(input())

for i in range(number):
    text = input()
    if 'Не' in text[0:3] or 'не' in text[0:3]:
        text = text[3:]
    print(text)
    
for i in res:
    print(i)
