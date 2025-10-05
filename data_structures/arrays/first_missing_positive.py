def first_missing_positive(nums: list[int]) -> int:
    """
    Find the smallest missing positive integer from the list.

    >>> first_missing_positive([3, 4, -1, 1])
    2
    >>> first_missing_positive([1, 2, 0])
    3
    """
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
