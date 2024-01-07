import pymorphy2

morph = pymorphy2.MorphAnalyzer()
csce = {"именительный":"nomn",
        "родительный":"gent",
        "дательный":"datv",
        "винительный":"accs",
        "творительный":"ablt",
        "предложный":"loct"}
word = morph.parse(input())[0]

if "NOUN" in word.tag.POS:
    print("Единственное число:")
    for i in csce:
        print(i, word.inflect({"sing", csce[i]}).word)
        
    print("Множественное число:")
    for i in csce:
        print(i, word.inflect({"plur", csce[i]}).word)
else:
    print('Не существительное')
