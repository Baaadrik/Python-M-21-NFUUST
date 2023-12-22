#русский алфавит
Alphabet = [chr(i) for i in range(ord('А'), ord('я'))]
result = []

def encrypt_caesar(msg, shift=3):
	for n in msg:
		if n in Alphabet:
			#данная конструкция делает шаг в списке
			if len(Alphabet) < Alphabet.index(n)+shift:
				#если шаг привышает длину списка
				#не работает, т.к. маленькие буквы становятся большими
				symbol = len(Alphabet) - (Alphabet.index(n)+shift)
			else:
				symbol = Alphabet.index(n)+shift
			result.append(Alphabet[symbol])
		else:
			result.append(n)
	return ''.join(result)

def decrypt_caesar():
	pass

print(encrypt_caesar('Да здравствует салат Цезарь!',5))