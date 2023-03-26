class Solution:                   #Solution class

	def factorial(self,n):          #find n th factorial number
		if(n==0):
			return 1

		factorial_num = 1

		for i in range(1,n+1):
			factorial_num *= i

		return factorial_num

	def digit_sum(self,num):        #find sum of digits in n th factorial number

		digit_sum_num = 0

		while (num != 0):
			digit = num % 10
			num = num // 10 

			digit_sum_num += digit

		return digit_sum_num

def main():
	x = Solution()
	y = x.digit_sum(x.factorial(100))
	print(y)

if __name__ == '__main__':
	main() 
