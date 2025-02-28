def removeElement(nums, val: int) -> int:
    # Initialize a pointer for the position to place the next non-val element
    write_pointer = 0

    # Iterate through the list
    for read_pointer in range(len(nums)):
        # If the current element is not equal to val, place it at the write_pointer position
        if nums[read_pointer] != val:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1

    # The first `write_pointer` elements are now the elements not equal to val
    return write_pointer


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
