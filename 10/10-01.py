a = int(input())
numbers = list()
flag = 'нет'

for i in range(a):
    x = int(input())
    numbers.append(x)
    
result = int(input())

for i in range(0, a - 1):
    for j in range(i + 1, a):
        if numbers[i] * numbers[j] == result:
            flag = 'да'
            break
print(flag)
