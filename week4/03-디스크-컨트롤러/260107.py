from heapq import heappop, heappush
from collections import defaultdict


def solution(jobs):
    job_map = defaultdict(list)
    for num, (ask, cost) in enumerate(jobs):
        job_map[ask].append((cost, ask, num))

    pq = []
    time = 0

    progressing = None
    finish_sum = 0
    finish_count = 0

    while finish_count != len(jobs):
        if job_map[time]:
            for job in job_map[time]:
                heappush(pq, job)

        if progressing and progressing[1] == time:
            finish_sum += (progressing[1] - progressing[0])
            finish_count += 1
            progressing = None
        if not progressing and pq:
            cur_cost, cur_ask, cur_num = heappop(pq)
            progressing = [cur_ask, time + cur_cost]

        time += 1

    return int(finish_sum / len(jobs))


print(solution([[0, 3], [1, 9], [3, 5]]))  # 8
