def gcdOfStrings(str1: str, str2: str) -> str:
    l1, l2 = len(str1), len(str2)
    size = min(l1, l2)
    common = ""
    for i in range(size):
        if str1[i:2*i] == str2[i:2*i] == common and common != "":
            break
        elif str1[i] == str2[i]:
            common += str1[i]
        else: break
    return common

str1, str2 = "ABABAB", "ABAB"
ans = gcdOfStrings(str1, str2)
print(ans)