M = int(input())
N = int(input())

set_1 = set()
for i in range(M):
	set_1.add(str(input()))

for i in range(N):
	text = str(input())
	if text in set_1:
		print('YES')
	else:
		print('NO')

