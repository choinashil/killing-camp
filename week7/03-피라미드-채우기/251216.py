from collections import defaultdict


def solution(blocks):
    memo = defaultdict(dict)

    for floor, (pos, val) in enumerate(blocks):
        memo[floor][pos] = val

    for cur_idx in range(1, len(blocks)):
        cur_pos, cur_val = blocks[cur_idx]
        cur_floor = memo[cur_idx]
        prev_floor = memo[cur_idx - 1]

        for pos in range(cur_pos, -1, -1):
            left = prev_floor.get(pos - 1)
            if left != None:
                val = memo[cur_idx][pos]
                cur_floor[pos - 1] = left - val

        for pos in range(cur_pos, cur_idx + 1):
            right = prev_floor.get(pos)
            if right != None:
                val = memo[cur_idx][pos]
                cur_floor[pos + 1] = right - val

    answer = []
    for f in memo:
        for i in range(0, f + 1):
            answer.append(memo[f][i])

    return answer


print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
