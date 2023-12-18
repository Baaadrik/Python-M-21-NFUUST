words = dict()
for word in input().split():
    if word not in words:
        words[word] = 0
    words[word] += 1
    print(words[word], end=" ")

