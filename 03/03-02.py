password = str(input())
password2 = str(input())

if len(password) < 8:
	print('Короткий!')
elif password != password2:
	print('Различаются.')
else:
	print('ОК')