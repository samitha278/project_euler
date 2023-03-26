class Solution:
    
    def isPrime(self,n):                                    #check number is prime number or not
        for j in range(2,int(n**0.5)+1):
            if (n%j == 0):
                return False
        return True

    def prime_number(self,lim):                             #prime number genarator
        for i in range(2,lim):
            if self.isPrime(i):
                yield i
                
    def circular_prime(self,lim):                           #check prime number circular or not
        
        circular_prime_list = []                            #circular prime number list
        
        for i in self.prime_number(lim):
        
            if (i<10):                                      #find circular prime numbers below 10.  
                circular_prime_list.append(i)               #(all prime numbers below 10 are circular prime numbers)
                continue
            
            if (i in circular_prime_list):       
                continue
            
            if (i<100):                                     #find circular prime numbers below 100
                str_rev_i = str(i)[::-1]
                rev_i = int(str_rev_i)
                if (i == rev_i):
                        circular_prime_list.append(i)
                elif self.isPrime(rev_i):
                        circular_prime_list.extend([i,rev_i])
                continue
             
            str_i = str(i)
            temp = []

            for j in range(len(str_i)):                     #rotate prime number 
                x = str_i[-1]+str_i[:-1]                    #if i==197 ; when j==0 ; x == "719"    

                if self.isPrime(int(x)):                    #check (int)x is prime or not
                    temp.append(int(x))                     #if x is prime loop again 
                    str_i = x
                else:                                       #if x is not prime break loop                      
                    break

            if (len(temp)==len(str(i))):                    #check temp is equal to length of str(i)
                circular_prime_list.extend(temp)

        return len(circular_prime_list)                     #return length of circular prime number list


def main():
    x = Solution()
    y = x.circular_prime(1000000)                           #find number of circular prime numbers below 1000000
    print(y)

if __name__ == '__main__':
    main()
