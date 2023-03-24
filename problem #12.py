def main():
    x = hdt_num()
    print(x)

def hdt_num():
    for i in triangular_num():
        j=0
        n = i**0.5
        for k in range(1,int(n)+1):
            if (i%k==0):
                j+=1
                
            if (n-int(n)) == 0:
                if(j*2-1 > 500):
                return i

            if(j*2 > 500):
                return i

def triangular_num():
    i = 0
    sum = 0
    while True:
        i+=1
        sum+=i
        yield sum

if __name__ == '__main__':
    main()
