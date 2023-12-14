#~/college/python-nfbgu/09/

num = int(input())
check = list()

for i in range(num):
    check.append(input())

search = input()

for i in range(len(check)):
    if search in check[i]:
        print(check[i])
