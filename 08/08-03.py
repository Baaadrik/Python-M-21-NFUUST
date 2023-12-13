text = input()
lags = {"_"}

for i in range(ord("a"), ord("z") + 1):
    lags.add(chr(i))

for char in text:
    if char not in lags:
        print('Неверный символ,', char)
        break
