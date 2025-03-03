def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    print(f"Merging {left_half} and {right_half}")
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    print(f"Result after merge: {sorted_array}")
    return sorted_array


# Example usage
nums = [5, 2, 3, 1]
sorted_nums = merge_sort(nums)
print("Final Sorted Array:", sorted_nums)
