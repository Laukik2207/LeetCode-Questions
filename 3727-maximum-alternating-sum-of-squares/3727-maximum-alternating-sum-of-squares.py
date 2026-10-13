class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([x * x for x in nums])

        n = len(squares)
        mid = n // 2
        smaller_sum = sum(squares[:mid])
        larger_sum = sum(squares[mid:])

        return larger_sum - smaller_sum