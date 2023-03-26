class Solution:

    def sum_factors(self,n):
        sum_fac = 0
        for i in range(1,n):
            if n%i == 0:
                sum_fac+=i
                
        return sum_fac
    
    def iter(self,limit):

        sum_amicable = 0

        for i in range(2,limit):
            sum1 = self.sum_factors(i)
            if sum1==1:
                continue
            sum2 = self.sum_factors(sum1)
            if sum2==1:
                continue

            if sum1==sum2:
                sum_amicable += sum1+sum2

        return sum_amicable


def main():
    x = Solution()
    y = x.iter(10000)
    print(y)

if __name__ == '__main__':
    main()
