english = int(input())
german = int(input())
set_english = set(); set_german = set();

for i in range(english):
	set_english.add(str(input()))
for i in range(german):
	set_german.add(str(input()))

if set_german ^ set_english:
	result = set_german ^ set_english
	print(len(result))
else:
	print('NO')