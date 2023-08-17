from itertools import permutations


def main():

    print(getLargestPrimePanDigital(9))


def getLargestPrimePanDigital(n):

    digits = [i for i in range(1,n+1)]

    largest = "".join(map(str,digits[::-1]))

    if isPrime(int(largest)):
        return largest

    j = 2
    while j<n+1:
        temp = largest[:-j]
        combi = list(map(lambda lst:''.join(lst),permutations(largest[-j:])))

        combi.pop()
        combi.sort(reverse=True)

        l = len(combi)
        k = 0
        while k<l:
            largest = temp + combi[k]
            if isPrime(int(largest)):
                return largest

            k+=1
            
        j+=1

    return getLargestPrimePanDigital(n-1)

    

    





def isPrime(n):

    if n<2:
        return n==2

    if n%2==0 or n%3==0 or n%5==0:
        return False

    lim = int(n**0.5)+1

    for i in range(7,lim,2): 

        if n%i==0:return False

    return True








main()


