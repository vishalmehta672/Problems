"""
169. Majority Element
Attempted
Easy
Topics
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3


Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
"""

nums = [3, 2, 2, 2, 3, 3, 3]

res = {}
n = len(nums)
for i in nums:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

print(res)


for num, count in res.items():
    if count > n // 2:
        print(num)


"""
def majorityElementSorting(nums):
    nums.sort()  # Sort the array
    n = len(nums)
    return nums[n // 2]  # The majority element is at the middle index

"""
