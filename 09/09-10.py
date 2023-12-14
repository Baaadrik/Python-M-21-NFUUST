#~/college/python-nfbgu/09/
a = int(input())
check = []
result = 0

for i in range(a):
    check.append(input())
c = int(input()) - 1
g = int(input())

while c != g:
    result += int(check[c])
    c += 1
print(result)
