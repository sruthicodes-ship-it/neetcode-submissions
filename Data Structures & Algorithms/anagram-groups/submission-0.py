class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnlist = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            returnlist[sortedS].append(s)
        return list(returnlist.values())
        