num = int(input())
list = []

for i in range(num):
    prod = input()
    if 'лук' not in prod:
        list.append(prod)

print(' , ' .join(list))
