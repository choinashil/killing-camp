from heapq import heappop, heappush


class Solution:
    def trapRainWater(self, heightMap):
        pq = []
        visited = set()

        row_len = len(heightMap)
        col_len = len(heightMap[0])

        for r in range(row_len):
            for c in range(col_len):
                h = heightMap[r][c]

                if r == 0 or r == row_len - 1 or c == 0 or c == col_len - 1:
                    heappush(pq, (h, r, c))
                    visited.add((r, c))

        cur_level = 0
        water = 0

        def in_range(r, c):
            return 0 <= r < row_len and 0 <= c < col_len

        while pq:
            print('==================================================')
            print('pq:', pq)
            cur_h, cur_r, cur_c = heappop(pq)
            print('cur_r:', cur_r, 'cur_c:', cur_c, 'cur_h:', cur_h)

            cur_level = max(cur_level, cur_h)
            print('cur_level:', cur_level)

            for dr, dc in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                print('------------인접 노드 순회-------------')
                next_r, next_c = cur_r + dr, cur_c + dc
                print('next_r:', next_r, 'next_c:', next_c)

                if in_range(next_r, next_c) and (next_r, next_c) not in visited:
                    next_h = heightMap[next_r][next_c]
                    print('cur_level:', cur_level, 'next_h:', next_h)

                    if next_h < cur_level:
                        print('높이 낮음 -> 물 채우기')
                        water += cur_level - next_h
                        print('추가할 물의 양:', cur_level - next_h)
                        heappush(pq, (cur_level, next_r, next_c))
                        visited.add((next_r, next_c))
                    else:
                        print('높이 낮지 않음 -> do nothing')
                        heappush(pq, (next_h, next_r, next_c))
                        visited.add((next_r, next_c))

        return water


if __name__ == '__main__':
    solution = Solution()
    print(solution.trapRainWater([[1, 1, 2], [1, 0, 2], [1, 1, 2]]))  # 1
    print(solution.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))  # 4
    print(solution.trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))  # 10
