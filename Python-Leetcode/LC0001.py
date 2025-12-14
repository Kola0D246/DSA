''' Easy | Two Sum

Given an array of integers `nums` and an integer `target`
Return indices of the two numbers from nums such that they add up to target.

Note: 
You may not use the same element twice
You can return the answer in any order

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Can you come up with an algorithm that is less than O(n2) time complexity?
'''


def twoSum(nums: list[int], target: int):
    length = len(nums)
    '''# O(n2) solution
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
    '''

    # O(n) complexity
    seen={}
    for i in range(length):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        
        seen[nums[i]] = i

    # no pair found
    return []

nums = [2,7,11,15]
target = 9
ans = twoSum(nums, target)
print(ans)