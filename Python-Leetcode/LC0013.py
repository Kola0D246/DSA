''' Easy | Roman to Integers

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol  Value
I       1
V       5
X       10
L       50
C       100
D       500
M       1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example:

Input: roman = "III"
Output: 3
Explanation: III = 3.

Input: roman = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: roman = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def romanToInt(roman: str) -> int:
    num = 0
    '''trick
    s=s.replace('IV','IIII')
    s=s.replace('IX','VIIII')
    s=s.replace('XL','XXXX')
    s=s.replace('XC','LXXXX')
    s=s.replace('CD','CCCC')
    s=s.replace('CM','MCCCC')
    for ch in roman:
        num+= dic[ch]
    return num
    '''

    lst = ""
    for ch in roman:
        print(lst, ch)
        if ((lst == 'I' and (ch == 'V' or ch == 'X')) or
            (lst == 'X' and (ch == 'L' or ch == 'C')) or
            (lst == 'C' and (ch == 'D' or ch == 'M'))):
            num+= (dic[ch]-2*dic[lst])
        else:
            num+= dic[ch]
        print(num)
        lst = ch
    return num

ans= romanToInt('LVIII')
print(ans)