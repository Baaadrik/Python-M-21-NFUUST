text = ''; i = 0;
while text != 'СТОП':
	i = i + 1
	text = str(input())
	if 'кот' in text:
		result = i

if bool(result) == True:
	print(result)
else:
	print(-1)
	