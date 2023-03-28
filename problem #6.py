class Solution:
    
    def sum_(self,n:int)->int:
        sum_nums = 0
        sum_sqrs = 0
        for i in range(1,n+1):
            sum_nums += i
            sum_sqrs += i**2
            
        return {"sum_nums":sum_nums,"sum_sqrs":sum_sqrs}
        
def main():
    x = Solution()
    y = x.sum_(100)
    diff = (y["sum_nums"]**2) - (y["sum_sqrs"])
    print(diff)
    
if __name__ == '__main__':
    main()
