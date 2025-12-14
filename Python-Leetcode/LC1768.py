def mergeAlternately(word1: str, word2: str):
    '''no need to do this
    lst1 = list(word1)
    lst2 = list(word2)
    '''
    '''Cpython-version for leetcode
    len1 = len(word1)
    len2 = len(word2)
    size = min(len1, len2)
    ans = ""
    for i in range(size):
        ans+= (word1[i]+word2[i])
    return ans + word1[size:] + word2[size:]
    '''
    len1 = len(word1)
    len2 = len(word2)
    size = min(len1, len2)
    ans = []
    for i in range(size):
        ans.append(word1[i])
        ans.append(word2[i])
    if len1>size:
        ans.extend(word1[size:])
    elif len2>size:
        ans.extend(word2[size:])
    return "".join(ans)



word1 = "ab"
word2 = "pqrs"
ans = mergeAlternately(word1, word2)
print(ans)