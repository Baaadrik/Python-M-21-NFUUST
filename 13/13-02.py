telephone = {}

n = int(input());
for i in range(n):
	phone, name = input().split()
	if name not in telephone:
		telephone[name] = list()
	telephone[name].append(phone)

n = int(input())
for i in range(n):
	name = input()
	if name in telephone:
		print(' '.join(telephone[name]))
	else:
		print('Нет в телефонной книге')
		