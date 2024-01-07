import pymorphy2
morph = pymorphy2.MorphAnalyzer()

for i in range(99, 0, -1):
    bottle = morph.parse('бутылка')[0]
    print("В холодильнике", i, bottle.make_agree_with_number(i).word, 
    	"кваса.\nВозьмём одну и выпьем.\nОсталось", i - 1, 
    	bottle.make_agree_with_number(i - 1).word, "кваса.")
    