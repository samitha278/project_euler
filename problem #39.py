def main():

    numSol = [getSolution(p) for p in range(1,1001)]

    maximumP = numSol.index(max(numSol)) +1
    print(maximumP)
    






def getSolution(p):

    n = p//2 + 1

    sols = [
        (i,j,k)
        for i in range(1,n)
        for j in range(1,n)
        if i<j<(k:=(p - (i+j))) and k**2 == i**2 + j**2
    ]        

    return len(sols)




main()
