num = int(input())
warfare = 'Евразия'; peace = 'Остазия';
for i in range(num):
	command = str(input())
	if 'С кем война?' == command:
		print(warfare)
	elif 'С кем мир?' == command:
		print(peace)
	elif 'Меняем' == command:
		change = warfare
		warfare = peace
		peace = change
