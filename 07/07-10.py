
l = int(input())
mstr = input().lower()
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
mlist = []

for i in mstr:
	mlist.append(alpha[(alpha.find(i) + l) % len(alpha)])
print('Result: ', '"', ''.join(mlist), '"', sep='')