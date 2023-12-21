Pi = 3.14159

def circle_length(radius):
	return 2 * Pi * radius

def circle_area(radius):
	return Pi * (radius ** 2)

def Main():
	R = float(input())
	print(str(circle_length(R)) + ' ' + str(circle_area(R)))

Main()