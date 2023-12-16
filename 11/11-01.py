s = input().split()
print([s[i] for i in range(len(s)) if (i+1) % 3 == 0])
