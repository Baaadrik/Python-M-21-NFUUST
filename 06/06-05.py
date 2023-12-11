ang = int(input())
nem = int(input())
frn = int(input())

intersection = set(); first = set(); second = set(); third = set()

cout = 0
for _ in range(ang + nem + frn):
    name = input()
    if name in second:
        third.add(name)
    elif name in first:
        second.add(name)
    else:
        first.add(name)

itog = (len(second) - len(third))

if itog > 0:
    print(itog)
else:
    print("NO")