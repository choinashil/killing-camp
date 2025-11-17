from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms):
        q = deque()
        visited = [False] * len(rooms)

        def bfs(start_v):
            q.append(start_v)
            visited[start_v] = True

            while q:
                cur_v = q.popleft()

                keys = rooms[cur_v]
                for key in keys:
                    if not visited[key]:
                        q.append(key)
                        visited[key] = True
        
        bfs(0)

        return all(visited)

if __name__ == '__main__':
    solution = Solution()
    print(solution.canVisitAllRooms([[1], [2], [3], []]))
    print(solution.canVisitAllRooms([[1], [2], [], []]))
