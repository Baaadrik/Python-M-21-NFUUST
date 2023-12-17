stroke = ((input().upper()).split(' '))
res = ''

for i in range(len(stroke)):
    res += '-'.join(list(stroke[i])) + ' '
    
res = res[:len(res)-1]
print(res)
