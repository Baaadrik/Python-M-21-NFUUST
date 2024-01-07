import pymorphy2

morph = pymorphy2.MorphAnalyzer()
g = ["masc", "femn", "neut"]
l = ["1per", "2per", "3per"]
word = morph.parse(input())[0]

if ("INFN" in word.tag.POS) or ("VERB" in word.tag.POS):
    print("Прошедшее время:")
    for i in g:
        print(word.inflect({'past', i}).word)
    print(word.inflect({'plur'}).word)
    
    print("Настоящее время:")
    for i in l:
        print(word.inflect({i, 'sing'}).word)
        print(word.inflect({i, 'plur'}).word)
else:
    print('Не глагол')