class Solution():

    def get_maximum_path(self,triangle):
        maximum = []
        sum = triangle[0][0]

        router = 0

        for i in range(1,len(triangle)):
            if(triangle[i][router] >= triangle[i][router+1]):
                sum += triangle[i][router]
            else:
                sum+= triangle[i][router+1]
                router+=1

        return sum 

def main():
    triangle = [[3],[7,4],[2,4,6],[8,5,9,3]]

    x = Solution()
    y = x.get_maximum_path(triangle)
    print(y)

if __name__ == '__main__':
    main()
