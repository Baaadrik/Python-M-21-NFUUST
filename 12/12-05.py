n = int(input()[1:])
f = 0

for n in range(n):
    s = input()
    f = s.find('#')
    print(s[:f])
