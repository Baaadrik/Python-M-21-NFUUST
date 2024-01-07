import pymorphy2
import sys
from pprint import pprint


def clear(text):
    return ''.join(filter(lambda c: c.isalpha() or c == '-', text))


morph = pymorphy2.MorphAnalyzer()
text = sys.stdin.read().split()
stat = dict()
for word in text:
    word = clear(word)
    parse = morph.parse(word)
    if not parse:
        continue
    parse = parse[0]
    print(parse)
    if parse.score > 0.5 and 'NOUN' in parse.tag:
        key = parse.normal_form
        stat[key] = stat.get(key, 0) + 1
res = list(stat.items())
res.sort(key=lambda c: (c[1], c[0]), reverse=True)
pprint(" ".join(list(map(lambda x: x[0], res))[:10]))