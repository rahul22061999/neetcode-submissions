class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 

        
        rows, cols = len(grid), len(grid[0])

        visit = set()
        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r,c))
            area = 0 

            while q:
                row, col = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
            
                area+=1
                for dx, dy in directions:
                    r, c = dx + row, dy + col 

                    if (
                        r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c]  and 
                        (r, c ) not in visit

                    ):
                       
                        visit.add((r,c))
                        q.append((r, c))
            return area




        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c) not in visit:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area
