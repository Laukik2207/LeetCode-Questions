class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n  = len(digits)
        # if n == 1:
        #     if(digits[0] == 9):
        #         digits[0] = 1
        #         digits.append(0)
        #         return digits
        #     else:
        #         digits[0] = digits[0]+1
        #         return digits
        num = 0
        for i in range(n):
            num *= 10
            num+=digits[i]
        num += 1
        i = 0
        arr = []
        while num > 0:
            arr.append(num%10)
            num = num // 10
            i+=1
        return arr[::-1]
                