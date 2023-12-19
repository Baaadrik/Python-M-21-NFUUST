def ask_password():
    a = 0
    password = "password"
    while True:
        b = input()
        a += 1
        if b == password and a <= 3:
            print("Пароль принят")
            a += 3
            return
        elif a == 3:
            print("В доступе отказано")
            return
