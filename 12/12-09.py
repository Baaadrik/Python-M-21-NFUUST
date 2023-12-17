a = input(); b = input();

for word in b.split():
    if a in word.lower():
        print(word)
