def main(): 
	sum_3_5 = multiples_sum()

	print(sum_3_5)

def multiples_sum():
	sum = 0

	for i in range(1000):
		if(i%3==0) or (i%5==0):
    			sum += i

	return sum

if __name__ == '__main__':
	main()
