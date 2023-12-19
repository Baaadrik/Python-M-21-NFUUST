def quarter(x, y):
    a = 'I четверть'
    b = 'II четверть'
    c = 'III четверть'
    d = 'IV четверть'
    
    if x < 0 and y > 0:
        return print(b)
    elif x > 0 and y > 0:
        return print(a)
    elif x < 0 and y > 0:
        return print(c)
    else:
        return print(d)

quarter(3, 4)
quarter(-3.5, 8)
