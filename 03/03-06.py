result = False

while result != True:
	pass1 = input()
	pass2 = input()
	if len(pass1) < 8:
		print('Короткий!')
	elif '123' in pass1:
		print('Простой!')
	elif pass1 != pass2:
		print('Различаются.')
	else:
		print('OK')
		result = True