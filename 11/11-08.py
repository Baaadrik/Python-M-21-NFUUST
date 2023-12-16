s = input()
s = s[s.index('?') + 1:].split('&')
obj = {}

for i in s:
	i = i.split('=')
	obj[i[0]] = i[1]

print(obj[input()])
