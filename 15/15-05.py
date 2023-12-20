l1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
      'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
      'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', '']
l2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
      'eighty', 'ninety']

def number_in_english(a):
    if not a:
        return 'zero'
    if a // 100 and a % 100:
        result = '{} hundred and '.format(l1[a // 100 - 1])
    elif a // 100:
        result = '{} hundred'.format(l1[n // 100 - 1])
    else:
        result = ''
    if a % 100 <= 19:
        result += l1[a % 100 - 1]
    else:
        result = result + l2[a % 100 // 10 - 2] + ' ' + l1[a % 10 - 1]
    return result
