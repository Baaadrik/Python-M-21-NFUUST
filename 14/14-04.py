def who_are_you_and_hello():
    w = input()
    while not all([w.isalpha(), w.istitle(), len(w.split()) == 1, w[1:].islower()]):
        w = input()
    print('Привет, {}!'.format(w))

who_are_you_and_hello()
