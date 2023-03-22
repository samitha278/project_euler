def factor(x):
    a = 0
    for i in range(2,int((x**0.5))+1):   #for small numbers ->  for i in range(2, x//2):
        if x % i == 0:
            if (isPrime(i) == True):
                a = i
    return a

def isPrime(i):
    j = 2
    k = 0
    while j <= i:
        if i % j == 0:
            k += 1
        if k > 1:
            return False
        j += 1
    return True

def main():
    x = factor(600851475143)
    print(x)

if __name__ == '__main__':
    main()
