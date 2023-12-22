
def emails(email='',name='', date='', geo='Нефтекамске'):
	print('To: ', email,
		f'\nЗдравствуйте,', name+'!'
		f'\nБыли бы рады видеть вас на встрече начинающих программистов в '+geo+
		f', которая пройдёт',date)

emails('simple@ya.ru', 'Данил', 'Нефтекамске', '18 апреля')
emails('simple@ya.ru', 'Айдар', '18 апреля')