def space_game(text):
    a = 0
    for i in text:
        if i == " ":
            a += 1
    if a % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")

space_game(input())
