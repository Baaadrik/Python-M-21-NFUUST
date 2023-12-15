a = int(input()); check = []; cr = 1;

for i in range(a):
    check.append(input())
    
b = int(input())
c = int(input())
res = check.copy()

while c != 0:
    check = res.copy()
    for i in range(len(check)):
        if cr == b:
            res.remove(check[i])
            cr = 0
        cr += 1
    c -= 1
    cr = 1

for i in range(len(res)):
    print(res[i])
