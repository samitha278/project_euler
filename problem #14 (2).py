class Solution:
    def collatz(self, n):
        longest_chain = 1
        max_items = 1
        
        collatz_dic = {1:1}
        
        for i in range(2, n+1):
            chain_items = 1
            p = i
            
            collatz_sub_dic = {}
            
            while p != 1:
                
                if p not in collatz_dic:
                    collatz_sub_dic[p] = chain_items
            
                    if p % 2 == 0:
                        p = p // 2
                    else:
                        p = 3 * p + 1
                        
                else:
                    chain_items += collatz_dic[p]
                    break
                
                chain_items += 1
                
            for j in collatz_sub_dic:
                collatz_sub_dic[j] = chain_items - collatz_sub_dic[j] + 1
                
            collatz_dic.update(collatz_sub_dic)

            if max_items < chain_items:
                max_items = chain_items
                longest_chain = i
        
        return longest_chain,max_items

def main():
    x = Solution()
    y = x.collatz(1000000)
    print("number:",y[0],"\nitems in chain:",y[1])

if __name__ == '__main__':
    main()
