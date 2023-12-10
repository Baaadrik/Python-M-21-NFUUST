
result = 0; num = 1; i = 0; suma = 0;
while num != 0:
	i += 1
	num = int(input())
	suma += num
	if suma == 10 and result == 0:
		result = i

if bool(result) == True: print(result)
