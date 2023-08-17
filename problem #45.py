def isPenta(p):
    x = 1+ (24*p +1)**0.5
    return x%6==0


def isHexa(h):
    x = 1+ (8*h +1)**0.5
    return x%4==0


def isTri(t):
    x = (8*t+1)**0.5  - 1
    return x%2==0


def nextTri(t):

    n = ((8*t+1)**0.5  - 1) //2
    tri1 = t
    
    while True:
        tri2 = tri1 + (n+1)

        if isPenta(tri2) and isHexa(tri2):
            return tri2
        
        n+=1
        tri1 = tri2
        
        if tri1 > 100000000000000000:
            return -1


print(nextTri(40755))



