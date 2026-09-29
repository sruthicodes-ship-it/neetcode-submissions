class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        hashmap = [[] for i in range(n)]
        for v1, v2 in edges:
            hashmap[v1].append(v2)
            hashmap[v2].append(v1)
        
        visiting = []
        count = 0

        def dfs(val,visiting):
            visiting.append(val)
            for v in hashmap[val]:
                if v not in visiting:
                    dfs(v, visiting)
            

        for i in range(n):
            if i not in visiting:
                count += 1
                dfs(i, visiting)
        
        return count
