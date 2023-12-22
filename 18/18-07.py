def solve(coefficients):
	if len(coefficients) == 3:
		a,b,c = coefficients[0],coefficients[1],coefficients[0]
		return (-b-(b**2-4*a*c)**0.5)/(2*a), (-b+(b**2-4*a*c)**0.5)/(2*a)
	elif len(coefficients) == 2:
		return -coefficients[1]/coefficients[0]
	elif len(coefficients) == 1:
		return 0
	else:
		return None

nums = list(map(int, input().split()))

print(sorted(solve(nums)))