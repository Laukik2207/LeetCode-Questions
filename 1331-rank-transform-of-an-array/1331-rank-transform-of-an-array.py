class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        mp = {x: i + 1 for i, x in enumerate(sorted(set(arr)))}
        return [mp[x] for x in arr]