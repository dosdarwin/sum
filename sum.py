
number=input('please type the numbers you are goint to sum(like:5,6,7):')
number2=[int(x) for x in number.split(',')]

def sum_of_list(numbers):
	return sum(numbers)

print(sum_of_list(numbers=number2))

