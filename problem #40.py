import math


def getDn(n):
    
    if n<1:
        return "impossible"
     

    global fraction

    tempFra = fraction["fra"]
    
    if n == 1:
        return int(tempFra[2])
        
        
    last = fraction["last"]

    l = len(tempFra) - 2
    p = last + 1
    
    while l<=n:

        temp = str(p)
        tempFra += temp

        l += len(temp)
        p += 1

    fraction["fra"] = tempFra
    
    return int(tempFra[n+1])






if __name__=="__main__":
    fraction = {"fra":'0.1',"last":1}
    
    #print(getDn(100))
    value = math.prod(getDn(10**i) for i in range(7))
    print(value)

