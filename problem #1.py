def main():
	multiples_sum_3 = multiples_sum(3,10)
	multiples_sum_5 = multiples_sum(5,10) 

	sum_3_5 = multiples_sum_3 + multiples_sum_5

	print(sum_3_5)

def multiples_sum(x,n):
	sum = 0

	for i in range(0,n,x):
    sum += i

	return sum

if __name__ == '__main__':
	main()
