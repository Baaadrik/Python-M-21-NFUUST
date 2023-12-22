scoring = {
	'Яблочко': 50,
	'Зеленое кольцо': 25,
	'Внешнее кольцо': {
		1: 8, 
		2: 6, 
		3: 42, 
		20: 50},
	'Внутреннее кольцо': {
		1: 2, 
		2: 9, 
		3: 56, 
		20: 3
	}
}

def score(name,sector=0):
	if sector == 0:
		return scoring[name]
	elif sector != 0:
		return scoring[name][sector]

print(score('Внешнее кольцо', 1))