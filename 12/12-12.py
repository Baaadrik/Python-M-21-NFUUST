a = input().lower()
b = []

for char in set(a):
    b.append(a.count(char))
print(max(b))
