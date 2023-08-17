def isPrime(n):

    if n<3:return n==2

    primes = [2,3,5,7,11,13,17,19]
    
    for i in primes:
        if n == i:
            return True
        if n%i==0:
            return False

    for i in range(23,int(n**0.5)+1):
        if n%i==0:
            return False

    return True




def goldbach():

    odd = 9
    
    while True:

        if not isPrime(odd):
            
            flag = False
            
            for i in range(odd-2,1,-2):
                if not isPrime(i):continue
                for j in range(1,int(odd**0.5)+1):
                    x = i + 2*(j**2)
                    if x==odd:
                        flag = True
                        break
                    
                if flag:break
            
            if not flag:
                return odd
                    
        odd +=2
        
        
print(goldbach())
