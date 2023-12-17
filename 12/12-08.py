s = input(); s1 = []; s2 = []; n = 0; res = '';

for i in s:
    if i != ' ':
        s1.append(i.lower())
        s2.append(i.lower())
s2.sort()

for i in s2:
    if s1.count(i) > n:
        n = s1.count(i)
        res = i
print(res)
