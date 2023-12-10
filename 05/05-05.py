i = 0; text = ' '; result = False;
while text != 'СТОП':
	text = str(input())
	i += 1
	if 'кот' in text or 'Кот' in text:
		result = i
		break

if bool(result) == True:
	print(result)
else: 
	print(-1)