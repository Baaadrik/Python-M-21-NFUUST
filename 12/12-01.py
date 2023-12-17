for i in range(int(input())):
    text = input()
    if 'кот' in text:
        print(i + 1, text.find('кот') + 1)
