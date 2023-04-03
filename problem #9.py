class Solution:

	def pythagorean(self,n):
		c = 0 
		while (c<n) :
			b = 0 
			while (b<c):
				a = 0
				while (a<b):
					x = a**2 + b**2
					if(x == c**2):
					    print(f"{a},{b},{c}")
					    yield (a,b,c)
					a+=1
				b+=1
			c+=1

	def check(self,n):
		for i in self.pythagorean(n):
			x = sum(i)

			if (x == 1000) :
				y = 1
				for j in i:
					y*=j
				return y

def main():
	solution = Solution()
	print(solution.check(1000))
	
if __name__ == '__main__':
	main()
