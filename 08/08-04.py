number = buf = int(input())
board = 'A'

for i in range(number*number):
    if (i+1) % number != 0:
        print(chr(ord(board)), buf, sep='', end=' ')
        board = chr(ord(board)+1)
    else:
        print(chr(ord(board)), buf, sep='')
        board = 'A'
        buf -= 1
