class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        char = sorted(freq.keys(),key = lambda x : freq[x],reverse = True)

        ans=[]
        for ch in char : 
            ans.append(ch * freq[ch])
        return "".join(ans)