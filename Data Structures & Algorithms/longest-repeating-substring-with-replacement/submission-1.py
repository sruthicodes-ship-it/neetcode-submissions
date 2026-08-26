class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0 
        chardic = {}
        for r in range(len(s)):
            chardic[s[r]] = 1 + chardic.get(s[r], 0)
            if (r-l+1) - max(chardic.values()) > k:
                chardic[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        
        return res
