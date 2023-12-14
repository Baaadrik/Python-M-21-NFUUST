#~/college/python-nfbgu/09/
a = int(input())
check = list()
res = list()

for i in range(n):
   check.append(input())

for i in range(len(check)):
     if i > 0:
         res.append(int(check[i]) + int(check[i - 1]))

for i in range(len(res)):
    print(res[i])
