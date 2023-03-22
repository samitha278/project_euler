def fibonacci(a):
	x = 0 
	y = 1

	yield y 

	z = 0 
	while (z<a):
		z = x+y 
		yield z 
		x = y 
		y = z

def sum_even_fibonacci(a):
	sum = 0
	for i in fibonacci(a):
		if (i%2==0):
			sum+=i

	return sum 

def main():
	sum_even_fib = sum_even_fibonacci(4000000)
	print(sum_even_fib)

if __name__ == '__main__':
	main()
