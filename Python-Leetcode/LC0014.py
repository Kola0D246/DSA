''' Easy | Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""      # There is no common prefix among the input strings.
'''

def commonPrefix(s1, s2):
    pre= []
    size=min(len(s1), len(s2))
    for i in range(size):
        if s1[i] != s2[i]:break
        pre.append(s1[i])
    return pre

def longestCommonPrefix(strs: list[str]) -> str:
    lsize = len(strs)
    # if strs has only single string
    if lsize==1:
        return strs[0]
    # if strs has more than 1 string
    pre= commonPrefix(strs[0], strs[1])
    for i in range(2, lsize):
        pre= commonPrefix(pre, strs[i])
        if pre == []: break
    return ''.join(pre)

ans= longestCommonPrefix(["dog","racecar","car"])
print(ans) if ans != '' else print("NAAAA")