num = input().split()
print(*[int(num[i]) ** 2 for i in range(len(num)) if (int(num[i]) ** 2) % 10 != 9 and int(num[i]) % 2 != 0])
