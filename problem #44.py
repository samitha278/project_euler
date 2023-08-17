
    
    
    
def findMinDiff():
    
    i= 1
    
    while True:
        
        j = 1
        while j<i:
            b = getPentagonal(i)
            a = getPentagonal(j)
            add = a+b
            diff = b-a
            
            if isPenta(add) and isPenta(diff): 
                return diff
            j+=1 
        i+=1
    



def getPentagonal(n):
    return (n*(3*n-1))//2




print(findMinDiff())




################################################################


def main(n):
    
    pentas = tuple(getPentagonal(i) for i in range(1,n))
    

    #minDiff = findMinDiff(n-1,pentas)
    
    minDiff = list( 
        j-i
        for ind,i in enumerate(pentas)
        for j in pentas[ind+1:]
        if isPenta(i+j) and isPenta(j-i)    
    )

    print(minDiff)
    

def isPenta(p):
    x = 1+ (24*p +1)**0.5
    
    return x%6==0    

#print(isPenta(145))
#main(1000000)
