set_city = set()
for i in range(int(input())):
	set_city.add(str(input()))
city = str(input())
if city in set_city:
	print('TRY ANOTHER')
else:
	print('OK')