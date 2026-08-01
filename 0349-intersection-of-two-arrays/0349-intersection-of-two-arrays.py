class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        ans = []

        for i in nums2:
            if i in s:
                ans.append(i)
                s.remove(i)
        return ans