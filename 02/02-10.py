#(+, -, * или /) 888888
num_1 = float(input())
num_2 = float(input())
text = str(input())

if text == '+':
	print(num_1+num_2)
elif text == '-':
	print(num_1-num_2)
elif text == '*':
	print(num_1*num_2)
elif  num_2 == float(0):
	print(888888)
elif text == '/':
	print(num_1/num_2)
else:
	print(888888)