class Solution:
    
    def isPrime(self,n):
        for j in range(2,int(n**0.5)+1):
            if (n%j == 0):
                return False
        return True

    def prime_number(self,lim):
        for i in range(2,lim):
            if self.isPrime(i):
                yield i
                
    def circular_prime(self,lim):
        
        circular_prime_list = []
        
        for i in self.prime_number(lim):
        
            if (i<10):
                circular_prime_list.append(i)
                continue
            
            if (i in circular_prime_list):
                continue
            
            if (i<100):
                str_rev_i = str(i)[::-1]
                rev_i = int(str_rev_i)
                if (i == rev_i):
                        circular_prime_list.append(i)
                else self.isPrime(rev_i):
                        circular_prime_list.extend([i,rev_i])
                continue
             
            str_i = str(i)
            temp = []

            for j in range(len(str_i)):
                x = str_i[-1]+str_i[:-1]

                if self.isPrime(int(x)):
                    temp.append(int(x))
                    str_i = x
                else:
                    break

            if (len(temp)==len(str(i))):
                circular_prime_list.extend(temp)

        return len(circular_prime_list)


def main():
    x = Solution()
    y = x.circular_prime(1000000)
    print(y)

if __name__ == '__main__':
    main()
