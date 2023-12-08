result = True
while True:
	text = str(input())
	if len(text) != 0 and result == True:
		print(text)
	elif len(text) == 0:
		result = False
		