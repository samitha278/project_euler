class Solution:
    def collatz(self, n):
        
        collatz_dic = {1:1}
        
        for i in range(2, n+1):
            
            if i in collatz_dic:
                continue
            else:    
                chain_items = 0
                p = i
                collatz_sub_dic = {}
                
                while p != 1:
                    
                    if p not in collatz_dic:
                        collatz_sub_dic[p] = chain_items 
                
                        if p % 2 == 0:
                            p = p // 2
                        else:
                            p = 3 * p + 1
                            
                    if p in collatz_dic:
                        chain_items += collatz_dic[p]+1
                        break
                    
                    chain_items += 1
                    
                for j in collatz_sub_dic:
                    collatz_sub_dic[j] = chain_items - collatz_sub_dic[j]
                    
                collatz_dic.update(collatz_sub_dic)
                
                collatz_sub_dic.clear()
                
        key_max = max(collatz_dic, key= lambda x: collatz_dic[x])
        
        return {"longest_chain":key_max , "chain_items":collatz_dic[key_max] }

def main():
    x = Solution()
    y = x.collatz(1000000)
    print("number:",y["longest_chain"],"\nitems in chain:",y["chain_items"])

if __name__ == '__main__':
    main()
