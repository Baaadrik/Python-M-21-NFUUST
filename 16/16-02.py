def discriminant(a,b,c):
	return (b**2)+(4*a*c)

def smaller_root(p,q):
	d = discriminant(1,p,q)
	return (-p+d**(0.5))/2

def larger_root(p,q):
	d = discriminant(1,p,q)
	return (-p-d**(0.5))/2

def Main():
	p = float(input())
	q = float(input())
	print(discriminant(1,p,q))
	print(str(larger_root(p,q)) + ' ' + str(smaller_root(p,q)))

Main()
