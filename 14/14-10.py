def golden_ratio(i):
    if i != 1:
        numbers = [1, 1]
        for n in range(2, i + 1):
            numbers.append(numbers[n - 1] + numbers[n - 2])
            if n == i:
                print(numbers[n] / numbers[n - 1])
    else: print('1.0')
