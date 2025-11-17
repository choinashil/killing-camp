from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        q = deque()

        row_len = len(grid)
        col_len = len(grid[0])

        dr = [-1, -1, -1, 0, 1, 1, 1, 0]
        dc = [-1, 0, 1, 1, 1, 0, -1, -1]

        def bfs(sr, sc, sd):
            if grid[sr][sc] == 0:
              q.append((sr, sc, sd))
              grid[sr][sc] = -1

            while q:
                r, c, d = q.popleft()

                if r == row_len - 1 and c == col_len - 1:
                    return d

                for i in range(8):
                    nr, nc = r + dr[i], c + dc[i]

                    if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 0:
                        q.append((nr, nc, d + 1))
                        grid[nr][nc] = -1

            return -1
        
        return bfs(0, 0, 1)
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(solution.shortestPathBinaryMatrix([[1,1],[1,0]]))
    print(solution.shortestPathBinaryMatrix([[0,1],[1,1]]))
    print(solution.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
    print(solution.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
