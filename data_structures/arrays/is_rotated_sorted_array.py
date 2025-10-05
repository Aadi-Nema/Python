def is_rotated_sorted(nums: list[int]) -> bool:
    """
    Check if the given array is a rotated sorted array.

    >>> is_rotated_sorted([3, 4, 5, 1, 2])
    True
    >>> is_rotated_sorted([2, 1, 3, 4])
    False
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i + 1) % len(nums)]:
            count += 1
            if count > 1:
                return False
    return True
