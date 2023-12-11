sets = set(); sets2 = set()
 
num = int(input())
 
k = 0
for i in range(num):
    family = input()
 
    if not family in sets:
        sets.add(family)
        sets2.add(family)
    elif family in sets2:
        k += 2
        sets2.remove(family)
    else:
        k += 1
 
print(k)