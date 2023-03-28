class Solutioin:
    def isPrime(self,n:int)->bool:
        for i in range(2,int(n**0.5)+1):
            if (n%i==0):
                return False
        return True
        
    def primeNum(self,n:int)->int:
        i = 2
        prime_num_counter = 0
        while True:
            if self.isPrime(i):
                prime_num_counter+=1
            if prime_num_counter == n:
                return i
            i+=1    
            
def main():
    x = Solutioin()
    y = x.primeNum(10001)
    print(y)
    
if __name__ == '__main__':
    main()
