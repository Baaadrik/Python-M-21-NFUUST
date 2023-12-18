def coun(x):
    dc[x] = dc.get(x, 0) + 1
    return dc[x]

dc = {}
print(*[coun(k) for k in input().split()])
