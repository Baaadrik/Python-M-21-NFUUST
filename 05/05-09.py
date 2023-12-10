result = False
for i in range(int(input())):
	text = str(input())
	if 'Кот' in text or 'кот' in text:
		result = True
	elif 'Пёс' in text or 'пёс' in text:
		result = False

if result == True:
	print('МЯУ')
elif result == False:
	print('НЕТ')