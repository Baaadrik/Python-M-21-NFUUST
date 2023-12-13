#/college/python-nfbgu/08/

number = int(input())

for i in range(number):
    text = input()
    if 'кот' in text:
        print(i+1, text.index('к')+1)
