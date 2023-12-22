result = [0]
def partial_sums(one, *num):
	summ = 0
	result.append(one)
	for i in range(len(num)):
		if i != 0:
			summ = summ + num[i]
		else:
			summ = num[i] + one
		result.append(summ)
	return result

print(partial_sums(1, 0.5, 0.25, 0.125))
