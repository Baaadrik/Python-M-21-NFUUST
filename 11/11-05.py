text = input().split()
s = ''
for i in range(len(text)):
    if i == 0:
        s = '["' + text[i] + '", '
    elif i == len(text) - 1:
        s += '"' + text[i] + '"]'
    else:
        s += '"' + text[i] + '", '
print(s)
