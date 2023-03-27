class Solution:
	def int_comb(self):
		seque = []
		for a in range(2,101):
			for b in range(2,101):
				x = a**b
				if x not in seque:
					seque.append(x)

		return len(seque)

def main():
	sol = Solution()
	print(sol.int_comb())
