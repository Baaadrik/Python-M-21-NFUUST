gold = float(input())

while int(gold/8) != 0 and int(gold/8) > 0:
	gold = gold-((int(gold / 8.0)*7)+(gold % 8.0))
print(int(gold))