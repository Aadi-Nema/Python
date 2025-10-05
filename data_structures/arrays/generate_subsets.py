def subsets(nums: list[int]) -> list[list[int]]:
    """
    Generates all possible subsets of a list of integers.

    >>> subsets([1, 2])
    [[], [1], [2], [1, 2]]
    """
    res = []

    def backtrack(start: int, path: list[int]):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res
