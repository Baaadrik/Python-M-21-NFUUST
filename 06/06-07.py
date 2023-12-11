b = set(); n = set();
listok = int(input())

for i in range(listok):
    family_num = int(input())
    for f in range(family_num):
        family = str(input())
        if family in b:
            n.add(family)
        else:
            b.add(family)

print('\n')
for i in b:
    print(i)