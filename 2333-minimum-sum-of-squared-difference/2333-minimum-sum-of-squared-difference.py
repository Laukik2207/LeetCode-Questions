class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        
        # Step 1: Calculate absolute differences and find the maximum difference
        max_diff = 0
        total_diff = 0
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            if diff > 0:
                total_diff += diff
                if diff > max_diff:
                    max_diff = diff
                    
        # Edge Case: If total available operations 'k' can clear all differences to 0
        if total_diff <= k:
            return 0
            
        # Step 2: Build a frequency array for the differences
        buckets = [0] * (max_diff + 1)
        for n1, n2 in zip(nums1, nums2):
            buckets[abs(n1 - n2)] += 1
            
        # Step 3: Greedily reduce the largest differences downwards
        for d in range(max_diff, 0, -1):
            if buckets[d] == 0:
                continue
                
            # Number of operations needed to bring all differences at 'd' down to 'd - 1'
            count = buckets[d]
            
            if k >= count:
                # We can shift all elements of value 'd' down to 'd - 1'
                k -= count
                buckets[d - 1] += count
                buckets[d] = 0
            else:
                # We can only shift 'k' elements down to 'd - 1'
                buckets[d - 1] += k
                buckets[d] -= k
                k = 0
                break
                
        # Step 4: Compute the minimum sum of squared differences
        ans = 0
        for d in range(1, max_diff + 1):
            if buckets[d] > 0:
                ans += buckets[d] * (d ** 2)
                
        return ans
