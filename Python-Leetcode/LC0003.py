'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "pwwkew"
Output: 3
Explanation: Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def lengthOfLongestSequence(string: str) -> int:
    # Example 2
    return len(set(string))

def lengthOfLongestSubstring(string: str) -> int:  
    # 19 ms - self
    lrg = 0
    seen = []
    for s in string:
        if s in seen:
            i = seen.index(s)
            seen = seen[i+1:]
        seen.append(s)
        if len(seen)>lrg:lrg = len(seen)
        print(s)
    return lrg

def lengthOfLongestSubstring0(string: str) -> int:  
    # 7 ms - sliding window solution - best
    maxlen = 0              # longest substring size
    left, right = 0, 0      # set left and right end of window
    seen = {}               # seen letters   

    while right < len(string):
        pos = seen.get(string[right])

        if pos is None or pos < left:
            maxlen = max(maxlen, right - left + 1)
        else:
            l = pos + 1
        
        seen[string[right]] = right
        right += 1

    return maxlen

ans = lengthOfLongestSubstring0("dvdf")
print(ans)