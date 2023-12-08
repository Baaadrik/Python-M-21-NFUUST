range_one, range_two = 1, 1000

print('500')
b = input()
while b != '=':
    if b == '>':
        range_two = range_two - (range_two - range_one) // 2
        x = range_two - (range_two - range_one) // 2
    elif b == '<':
        range_one = range_one + (range_two - range_one) // 2
        x = range_one + (range_two - range_one) // 2
        
    print(x)
    b = input()