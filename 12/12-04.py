a = [int(i) for i in input().split()]
MK = [int(i) for i in input().split()]
res = 0

for i in range(MK[0], MK[1] + 1):
	res += a[i]** 2
print(res)
