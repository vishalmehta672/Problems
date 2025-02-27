def preprocess_prefix_sum(nums, i, j):
    """Preprocess the array to create a prefix sum array."""
    # 1. p = [0,0,0,0,0,0]
    # get first value of num
    # 2. p[i] = p[i-1] + num[i]
    # 3. p[j+1] - i
    p = [0] * len(
        nums,
    )
    p[0] = nums[0]
    for k in range(1, len(nums)):
        p[k] = p[k - 1] + nums[k]

    if i == 0:
        print(p[j])
    else:
        res = p[j] - p[i - 1]

        print(res)


# Example usage:
nums = [1, 2, 3, 4, 5, 6]
i = 0
j = 3

preprocess_prefix_sum(nums, i, j)
