#~/college/python-nfbgu/09/
a = int(input())
check = []
result = []

for i in range(a):
    check.append(int(input()))

for i in range(len(check)):
    result.append(int(check[i]) * 3)

for i in range(len(check)):
    print(check[i])

print('')
for i in range(len(result)):
    print(result[i])
