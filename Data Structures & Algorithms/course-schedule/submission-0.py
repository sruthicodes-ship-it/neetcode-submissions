class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {}
        for i in range(numCourses):
            hashmap[i] = []
        
        for key,val in prerequisites:
            hashmap[key].append(val)

        visiting = []

        def dfs(node):
            if node in visiting:
                return False
            
            if hashmap[node] == []:
                return True
            
            visiting.append(node)

            for val in hashmap[node]:
                if not dfs(val):
                    return False

            visiting.remove(node)
            hashmap[node] = []
            return True
            
        for val in hashmap:
            if not dfs(val):
                return False

        return True    
            

