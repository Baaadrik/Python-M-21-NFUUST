bulls, cows = 0
text_one = input()
text_two = input()

if len(text_one) == len(text_two):
    for i in range(len(text_one)):
        if text_one[i] == text_two[i]:
            bulls += 1
        elif text_one[i] in text_two:
            cows += 1
            
print(bulls, cows)
