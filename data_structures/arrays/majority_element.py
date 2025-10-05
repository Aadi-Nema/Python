def majority_element(nums: list[int]) -> int:
    """
    Returns the majority element in the list using the Boyer-Moore Voting Algorithm.

    >>> majority_element([3, 2, 3])
    3
    >>> majority_element([2, 2, 1, 1, 1, 2, 2])
    2
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
