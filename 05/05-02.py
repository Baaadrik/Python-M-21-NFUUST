repeat = int(input())

flag = False
for i in range(repeat):
	text = str(input())
	if ('кот' in text) or ('Кот' in text):
		flag = True

if flag == True:
	print('МЯУ')
elif flag == False:
	print('НЕТ')
