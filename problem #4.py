class Solution:

	def highestPalindrome(self):

		palindrome = 0

		for i in range(999,99,-1):
		 	for j in range(999,99,-1):
		 		
		 		num = i*j
		 		
		 		str_num = str(num)
		 		reverse_str_num = str_num[::-1]

		 		if str_num == reverse_str_num:
		 			if palindrome<num:
		 			    palindrome=num

		return palindrome

def main():
	highest_palindrome = Solution().highestPalindrome()
	print(highest_palindrome)

if __name__ == '__main__':
	main()
