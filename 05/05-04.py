repeat = int(input())

for i in range(repeat):
	text = str(input())
	if ('Кот' in text) or ('кот' in text):
		result = True
		break

if result == True:
	print('МЯУ')
else:
	print('НЕТ')
	