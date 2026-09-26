class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Step 1: Create a hash map from knowledge pairs
        mapping = {key: value for key, value in knowledge}
        
        res = []
        i = n = len(s)
        j = 0
        
        # Step 2: Traverse the string
        while j < n:
            if s[j] == '(':
                # Find the closing bracket
                end = s.find(')', j)
                key = s[j + 1:end]
                # Append value from map or '?' if missing
                res.append(mapping.get(key, '?'))
                j = end + 1
            else:
                res.append(s[j])
                j += 1
                
        return "".join(res)
