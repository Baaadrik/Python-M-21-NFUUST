text = ' '; i = 0; result = 0;
while text != 'СТОП':
	i += 1
	text = str(input())
	if 'Кот' in text or 'кот' in text:
		if result == 0:
			one_result = i
		result += 1

if bool(result) == True:
	print(result, one_result, sep=' ')
else:
	print(result, -1, sep=' ')