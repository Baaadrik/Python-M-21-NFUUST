city_0 = input()
city_1 = input()

if city_0 == city_1:
	print('НЕТ')
elif (city_0 == 'Тула' and city_1 == 'Пенза') or (city_1 == 'Тула' and city_0 == 'Пенза'):
	print('НЕТ')
elif city_0 == 'Тула' or city_0 == 'Пенза':
	print('ДА')
elif city_1 == 'Тула' or city_1 == 'Пенза':
	print('ДА')
else:
	print('Loading..')