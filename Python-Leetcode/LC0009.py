''' Easy | Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise; without converting number to string
 
Example:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

def isPalindrome(x: int) -> bool:
    '''convert to string
    stx = string(x)
    return srx == srx[::-1]
    '''

    #edge case - if x is negative or if x-reverse have leadeing zeros (like 1230 -> 0321)
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    xr=0
    '''using list
    xc=x
    lst=[]
    while xc > 0:
        lst.append(xc%10)
        xc//=10

    xr=0
    for n in lst:
        xr*10
        xr+=n
    '''

    '''full reversal: O(n) complexity
    xc=x
    while xc>0:
        xr *= 10
        xr += xc%10
        xc //=10
    '''

    #half reversal: O(n/2) complexity
    while x>xr:
        xr *= 10
        xr += x%10
        x //= 10
        print(x, xr)

    #even digits: x == xr | 1221: x=12, xr=21
    #odd digits: x == xr%10 | 12321: x=12, xr=123
    return x == xr or x == xr//10

ans= isPalindrome(121)
print(ans)