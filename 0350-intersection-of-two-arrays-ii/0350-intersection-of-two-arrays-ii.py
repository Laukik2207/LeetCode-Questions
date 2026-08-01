class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        count = Counter(nums1)

        for i in nums2:
            if count[i] > 0:
                ans.append(i)
                count[i] -= 1
        return ans