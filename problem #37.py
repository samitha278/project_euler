def main():

    getPrimeSeive(1000000)
    
    nums = getTruncatablePrimes(11)

    print(sum(nums))



def getTruncatablePrimes(n):

    nums = []

    track = 0
    num = 22
    
    while track<n:
        numS = str(num)
        
        if right_left(numS):
            if left_right(numS):
                nums.append(int(num))
                track+=1
                print(nums)
        
        num+=1        
        

    return nums
                
        
        
def right_left(num):

    l = len(num)
    n = l
    while 0<n:
        temp = num[:n]
        if not pmsve[int(temp)]:
               return False
        n-=1
            
    return True


    
def left_right(num):

    l = len(num)
    n = 0
    while n<l:
        temp = num[n:]
        if not pmsve[int(temp)]:
               return False
        n+=1
            
    return True




#create prime sieve
pmsve = []

def getPrimeSeive(n):

    global pmsve
    
    pmsve = [True]*(n+1)

    pmsve[0],pmsve[1] = False,False
    
    sqrt = int(n**0.5)

    for i in range(2,sqrt+1):
        if pmsve[i]:
            for j in range(i*i,n+1,i):
                if pmsve[j]:
                    pmsve[j]=False

    return pmsve



main()
