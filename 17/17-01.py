def words(word):
	if word not in set_1:
		set_1.add(word)
	elif word in set_1:
		print(word)

set_1 = set()
while True:
	words(str(input()))