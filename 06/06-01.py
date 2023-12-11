i = 0; set_1 = set(); set_2 = set();
while i != 2:
	text = input()
	if text == '':
		i += 1
	elif text == '' and i == 1:
		break
	elif i == 1:
		set_2.add(text)
	else:
		set_1.add(text)

if set_1 & set_2:
	result = set_1 & set_2
	for i in result:
		print(str(i))
else:
	print('EMPTY')