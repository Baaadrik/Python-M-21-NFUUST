import pymorphy2
import sys

morph = pymorphy2.MorphAnalyzer()
j = morph.parse('живой')[0]

for i in sys.stdin:
    word = morph.parse(i.replace('\n', ''))[0]
    if word.tag.animacy == 'anim':
        if word.tag.number == 'plur':
            print(j.inflect({str(word.tag.number), 'nomn'}).word.capitalize())
        else:
            print(j.inflect({str(word.tag.number), str(word.tag.gender), 'nomn'}).word.capitalize())

    if word.tag.animacy == 'inan':
        if word.tag.number == 'plur':
            print('Не ' + j.inflect({str(word.tag.number), 'nomn'}).word)
        else:
            print('Не '+ j.inflect({str(word.tag.number), str(word.tag.gender), 'nomn'}).word)
            
    if word.tag.animacy == None:
        print('Не существительное')