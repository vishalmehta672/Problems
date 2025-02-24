# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true


# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


def hasDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


print(hasDuplicate([1, 1, 2, 3, 4]))  # False
# print(hasDuplicate([1, 2, 3, 2]))  # True


def hasDuplicate2(nums):
    return len(nums) != len(set(nums))


print(hasDuplicate([1, 2, 3, 4]))  # False
