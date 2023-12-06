login = input('Введите желаемый логин: ')
email = input('Введите почту: ')

if ('@' not in login) and ('@' in email):
	print('OK')
elif ('@' in login) and ('@' not in email):
	print('Некорректный логин и адрес')
elif ('@' in login):
	print('Некорректный логин')
elif ('@' not in email):
	print('Некорректный адрес')