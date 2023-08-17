from itertools import permutations


def main():

    permu = list(permutations('0123456789'))

    result = sum(int("".join(p)) for p in permu if isCond("".join(p)))

    return result


def isCond(p):
    
    primes = [2,3,5,7,11,13,17]

    for i in range(1,8):
        k = p[i:i+3]
        if not (int(k)%primes[i-1] == 0):
            return False

    return True

print(main())           
#print(isCond('1406357289'))














































        

