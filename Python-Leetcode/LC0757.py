''' Hard | Set Intersection Size At Least Two

Given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.
'''

# ANALYSIS
# Minimum return value = 2
# Maximum return value = 2*num_of_sets
# Find number of common elements 

intervals = [[1,3], [3,7], [8,9]]
set_list = []
for i in intervals:
    set_list.append(set(range(i[0], i[1]+1)))

def interactions(list_set:list[set]):
    set0 = list_set[0] & list_set[1]
    for s in range(2, len(list_set)):
        set0 = set0 & list_set[s]

    return set0

print(set_list)
I = interactions(set_list)

def check_common(S, I):
    common = S & I
    return len(common)

dictionary = {}
for i in range(len(set_list)):
    dictionary[i] = check_common(set_list[i], I)

print(dictionary)


if I == set():
    print(6)
if len(I) >= 2:
    print(2)
