class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat) , len(mat[0])

        left = 0
        right = n-1

        while(left <= right):
            mid = (left+right) // 2
            maxrow = 0

            for i in range(m):
                if(mat[i][mid] > mat[maxrow][mid]):
                    maxrow = i

            leftval = mat[maxrow][mid-1] if mid > 0 else -1
            rightval = mat[maxrow][mid+1] if mid < n-1 else -1

            if mat[maxrow][mid] > leftval and mat[maxrow][mid] > rightval:
                return [maxrow,mid]
            elif leftval > mat[maxrow][mid]:
                right = mid-1
            else:
                left = mid+1