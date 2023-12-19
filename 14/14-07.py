def print_statistics(arr):
    b = len(arr)
    if b == 0:
        for i in range(5):
            print(0)
        return

    print(n)
    avg = 0; min_arr = arr[0]; max_arr = arr[0]

    for a in arr:
        avg += a
        if a > max_arr:
            max_arr = a
        if a < min_arr:
            min_arr = a
    avg = avg/b

    print(avg)
    print(float(min_arr))

    print(float(max_arr))
    tmp = sorted(arr)
    
    if b % 2 == 0:
        med = 0.5*(tmp[b // 2-1] + tmp[b // 2])
    else:
        med = tmp[b // 2]
    print(float(med))
