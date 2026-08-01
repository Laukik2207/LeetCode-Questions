class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(left, right):
            if left == right:
                return nums[left]

            pick_left = nums[left] - dfs(left + 1, right)
            pick_right = nums[right] - dfs(left, right - 1)

            return max(pick_left, pick_right)

        return dfs(0, len(nums) - 1) >= 0