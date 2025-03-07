def twoSum(numbers, target: int):
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]

        if current_sum < target:
            left += 1
        else:
            right -= 1
    return []


numbers = [2, 7, 11, 15]
target = 9

print(twoSum(numbers, target))
