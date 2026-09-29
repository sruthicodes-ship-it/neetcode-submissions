class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        
        hashmap = {}
        for i in range(n):
            hashmap[i] = []
        
        for key,val in edges:
            hashmap[key].append(val)
            hashmap[val].append(key)

        print(hashmap)

        visiting = []
        def dfs(node, parent):
            if node in visiting:
                return False
            
            visiting.append(node)

            for val in hashmap[node]:
                if val == parent:
                    continue
                if not dfs(val, node):
                    return False
            
            return True 

        
        return dfs(0, -1) and n == len(visiting)
