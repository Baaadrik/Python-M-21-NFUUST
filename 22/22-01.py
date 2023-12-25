import random

def make_bingo():
    checklist = random.sample(range(1, 76), 24)
    res = checklist[:12] + [0] + checklist[12:]
    return print(tuple(res[:5]), tuple(res[5:10]), tuple(res[10:15]), tuple(res[15:20]), tuple(res[20:25]), sep='\n')

res = make_bingo()
