class Solution:
    def intToRoman(self, num: int) -> str:
        value = [
            1000,900,500,400,
            100,90,50,40,
            10,9,5,4,1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        ans=[]
        for i in range(len(value)):
            while(num >= value[i]):
                ans.append(symbols[i])
                num -= value[i]
        
        return "".join(ans)

