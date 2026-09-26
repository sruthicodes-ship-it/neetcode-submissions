class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1,0], [0, 1], [0, -1]]
        Rows, Cols = len(grid), len(grid[0])
        island = 0

        def dfs(r, c):
            if(r < 0 or r >= Rows or c < 0 or c >= Cols or grid[r][c] == "0"):
                return               
            
            grid[r][c] = "0"
            
            for dr, dc in directions:
                dfs(dr+r, dc+c)
        
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1":

                    dfs(r,c)
                    island += 1
        
        return island

        