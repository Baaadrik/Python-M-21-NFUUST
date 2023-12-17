for i in range(int(input())):
    a = input().split()
    b = a.index(min(a))
    
    if (all(a[i] >= a[i + 1] for i in range(b))
            and all(a[i] <= a[i + 1] for i in range(b, len(a) - 1))):
        a.sort(reverse=True)
        print(' '.join(a))
    else:
        print('НЕТ')
