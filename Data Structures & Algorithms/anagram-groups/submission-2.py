class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #returnlist = defaultdict(list)
        #for s in strs:
        #    sortedS = ''.join(sorted(s))
        #    returnlist[sortedS].append(s)
        #return list(returnlist.values())
        words_dict = {}
        output_list = []
        for i,v in enumerate(strs):
            search_word = ''.join(sorted(v))
            if search_word in words_dict:
                words_dict[search_word].append(v)
            else:
                words_dict[search_word] = [v]
        
        return  list(words_dict.values())
            