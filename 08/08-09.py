#/college/python-nfbgu/08/

number = int(input())

for i in range(number):
    text = input()
    if text[0:4] in '####':
        continue
    elif text[0:2] in '%%':
        print(text[2:])
    else:
        print(text)
