#/college/python-nfbgu/08/
length = int(input())
number = int(input())
res = ''

for i in range(number):
    text = input()

    if len(text) > 4:
        if len(text) > length+3:
            print(text[:-(len(text)-length+3)], '...', sep='')
        else:
            print(text)
