a = int(input())
b = [list(map(int,input().split())) for _ in range(a)]
c = dict()

for i in range(a):
    s = b[i][0] // 10, b[i][1] // 10
    if s not in s:
        c[s] = 0
    c[s] += 1
    
print(max(c.values()))
