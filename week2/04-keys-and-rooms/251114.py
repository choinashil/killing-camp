from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms):
        def bfs(room):
            q.append(room)
            visited.add(room)

            while q:
                cur_room = q.popleft()
                for next_room in rooms[cur_room]:
                    if next_room not in visited:
                        q.append(next_room)
                        visited.add(next_room)

        q = deque()
        visited = set()
        bfs(0)

        return len(rooms) == len(visited)


if __name__ == '__main__':
    solution = Solution()
    print(solution.canVisitAllRooms([[1], [2], [3], []]))
    print(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
