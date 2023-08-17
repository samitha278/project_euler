def largestPanDigital(n):

    largestPD = 0

    p = 1

    while True:
        
        pStr = str(p)  
        
        if len(pStr) > (n//2):
            break
        
        fD1 = int(str(largestPD)[0])
        fD2 = int(pStr[0])
        
        if fD1>fD2:
            p+=1
            continue
        
        i = 2
        num = str(p)
        l = len(num)
        while l!=n and l<(n+1):
            temp = str(p*i)
            t = len(temp)
            
            if (l+t) > 9 :
                break
            
            num += temp
            
            l = len(num)
            i+=1
        
        #print("tempory num  :  ",num)
        
        if i==2:
            break
    
        if l<9:
            p+=1
            continue

        number = int(num)
        
        if isPandigital(num) and number>largestPD:
            largestPD = number

        p+=1

    return largestPD
    
    
def isPandigital(num):
    return all(str(i) in num for i in range(1,10))
    
    
    


print(largestPanDigital(9))
