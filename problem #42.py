def main():


    text = readFile(input().strip())
    if text is None:return -1

    alpha = [chr(i) for i in range(ord("A"),ord("Z")+1)]

    count = sum(
        1
        for word in text
        if isTri(sum(alpha.index(char)+1 for char in word))
    )
    
    return count




def isTri(n):

    i = int((2*n)**0.5)

    tri =  getTri(i)

    above = 0
    below = 0

    while not (above>0 and below>0):
        #print(i,end=" ")
        if tri==n:
            return True

        if tri<n:
            i+=1
            below += 1
        elif tri>n:
            i-=1
            above += 1
        
        tri = getTri(i)
        
    return False

  
def getTri(n):
    return (n*(n+1))//2




def readFile(inpFile):
    try:
        with open(inpFile) as file:
            temptext = file.read()
            text = temptext[1:-1].split('","')

    except Exception as e:
        print(e)
        return
    
    return text

#print(readFile("input.txt"))











if __name__=="__main__":
    print(main())
    



