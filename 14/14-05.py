def triangle(a, b, c):
    max = a
    if b > a:
        max = b
    if c > max:
        max = c
    if max >= a+b+c-max:
        return print("Это не треугольник")
    else:
        return print("Это треугольник")

triangle(1, 1, 2)
triangle(7, 6, 10)
