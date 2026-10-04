class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}

        def dsf(i):

            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if ((i+len(w)) <= len(s) and s[i: i+len(w)] == w):
                    if (dsf(i+len(w))):
                        memo[i] = True
                        return True 
                
            memo[i] = False
            return False 
        return dsf(0)            

        