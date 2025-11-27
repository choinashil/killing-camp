from heapq import heappop, heappush
from collections import defaultdict


def solution(jobs):
    waiting = []
    progressing = None
    completed = []
    time = 0

    map = defaultdict(list)
    for i, (s, l) in enumerate(jobs):
        map[s].append((l, s, i))

    while len(completed) < len(jobs):
        if map[time]:
            for job in map[time]:
                heappush(waiting, job)

        if progressing and progressing[1] == time:
            completed.append(progressing[1] - progressing[0])
            progressing = None

        if waiting and not progressing:
            nl, nt, ni = heappop(waiting)
            progressing = (nt, time + nl)

        time += 1

    return sum(completed) // len(jobs)


print(solution([[0, 3], [1, 9], [3, 5]]))
