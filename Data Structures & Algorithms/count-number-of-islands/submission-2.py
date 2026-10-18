class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [[0,1],[1,0],[-1,0],[0,-1]]
        visit = set()
        #(i,j)
        islands = 0
        rows,cols = len(grid),len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col = q.pop()
                for dr,dc in d:
                    ro,co = row+dr,col+dc
                    if ro in range(rows) and co in range(cols) and grid[ro][co] == '1' and ((ro,co)) not in visit:
                        q.append((ro,co))
                        visit.add((ro,co))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands