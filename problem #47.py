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



def getPrimeFactors(n):

    pfac = set()
    
    for i in range(2,n):
        if n%i==0 and isPrime(i):
            pfac.add(i)

    return len(pfac)



def getDistinctPrimes():
    i = 2*3*5*7
    #i = 134040
    queue = []
    
    while True:
        print(i)
        
        if isPrime(i):
            i+=1
            queue = []
            continue
        
        l = len(queue) 
        r = 4-l 
        
        for j in range(r):
            n = i+j
            k = getPrimeFactors(n)
            
            if k!=4:
                queue = []
                i+=(j+1)
                flag = True
                break
            queue.append((n,k))
        
        if len(queue)==4:
            return queue[0][0]
            
        if flag:
            continue
            
        i+=r   
    


print(getDistinctPrimes())


        
        



