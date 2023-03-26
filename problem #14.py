class Soluion:

    def collatz(self,n):
        
        longest_chain = 1
        max_items = 1
        
        for i in range(2,n+1):

            chain_items = 1
            p = i

            while (p!=1):
            	if (p%2==0):
                    p = p//2
                else:
                    p = 3*p + 1

                chain_items += 1
            
            if max_items < chain_items:
                max_items = chain_items
                longest_chain = i

        return longest_chain

def main():
    x = Soluion()
    y = x.collatz(1000000)

    print(y)

if __name__ == '__main__':
    main()
