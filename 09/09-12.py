#~/college/python-nfbgu/09/
a = input()
b = int(a[:a.index(' ')])
total = int(a[a.index(' '):])
errors, true_total = [], 0

for i in range(b):
    primer = input()
    price = int(primer[:primer.index('*')])
    amount = int(primer[primer.index('*')+1:primer.index('=')])
    cost = int(primer[primer.index('=')+1:])
    if price * amount != cost:
        errors.append(i+1)
    true_total += price * amount
    
print(total - true_total)
for x in errors:
    print(x, end=' ')
