numbers = ['1', '3', '4', '2']
print(id(numbers))
numbers.sort()
print(id(numbers))

print('\n')

numbers2 = ['1', '3', '4', '2']
numbers3 = sorted(numbers2)
print(id(numbers2))
print(id(numbers3))