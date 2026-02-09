from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    max_count = [0] * 11
    memo = defaultdict(int)

    for order in orders:
        for c in course:
            for comb in combinations(sorted(order), c):
                comb_str = ''.join(comb)
                memo[comb_str] += 1
                max_count[len(comb_str)] = max(max_count[len(comb_str)], memo[comb_str])
    return sorted([k for k, v in memo.items() if v >= 2 and v == max_count[len(k)]])


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
