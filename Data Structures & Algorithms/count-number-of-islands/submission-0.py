class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col = q.popleft()
                visit.add((rows, cols))
                directions = [[0,1], [1,0], [-1,0], [0,-1]]

                for dx, dy in directions:
                    r , c = dx + row, dy + col

                    if (r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] == "1" and 
                        (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))



        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands +=1 
                    bfs(r, c)
    
        
        return islands