def sum_double_base_palindromes(n):
    return sum(
        i
        for i in range(n)
        if isPalindrome(str(i)) and isPalindrome(str(bin(i))[2:])
    )



def isPalindrome(string):
    return string==string[::-1]



print(sum_double_base_palindromes(1000000))
