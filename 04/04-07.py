num = int(input())

n = 0
for i in range(num):
	if num % (i+1) == 0:
		print(i+1, end=' ')
		n += 1

if n == 2:
	print('\nПРОСТОЕ')
else:
	print('\nНЕТ')