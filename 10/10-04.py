a = int(input())
b = []

for i in range(a):
    b.append(input())

for i in range(a - 1):
    for j in range(a - 1 - i):
        if len(b[j]) > len(b[j + 1]):
            b[j], b[j + 1] = b[j + 1], b[j]
        elif len(b[j]) == len(b[j + 1]):
              if b[j] > b[j + 1]:
                  b[j], b[j + 1] = b[j + 1], b[j]
                  
for i in range(len(b)):
    print(b[i])
