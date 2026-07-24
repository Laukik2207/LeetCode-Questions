class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set(nums)
        MAXX = 2048

        pair_xor = [False] * MAXX
        for x in s:
            for y in s:
                pair_xor[x ^ y] = True

        ans = [False] * MAXX
        for xy in range(MAXX):
            if pair_xor[xy]:
                for z in s:
                    ans[xy ^ z] = True
        return sum(ans)