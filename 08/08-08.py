#/college/python-nfbgu/08/
text = input()
count = maximum = 0

for i in range(len(text)):
    if text[i] == 'о':
        count += 1
    else:
        maximum = count
        count = 0
        
print(maximum)
