def max_subarray_sum(nums: list[int]) -> int:
    """
    Kadane's Algorithm to find the maximum subarray sum.

    >>> max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> max_subarray_sum([1])
    1
    """
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
