text = str(input())
num = int(input())

if len(text) >= num:
	print(text[num-1])
else:
	print('Ошибка')