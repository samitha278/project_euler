class Solution:
    def collatz(self, n):
        longest_chain = 1
        max_items = 1
        
        collatz_dic = {1:1}
        
        for i in range(2, n+1):
            chain_items = 1
            p = i

            while p != 1:
                if p % 2 == 0:
                    p = p // 2
                else:
                    p = 3 * p + 1
                    
                if p in collatz_dic:
                    chain_items += collatz_dic[p]
                    
                    collatz_dic[i] = chain_items
                    break
                
                chain_items += 1
                
            if i not in collatz_dic:
                collatz_dic[i] = chain_items

            if max_items < chain_items:
                max_items = chain_items
                longest_chain = i
        
        return longest_chain,max_items

def main():
    x = Solution()
    y = x.collatz(100)
    print("number:",y[0],"\nitems in chain:",y[1])

if __name__ == '__main__':
    main()
