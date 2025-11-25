from heapq import heappop, heappush
from collections import defaultdict


def solution(jobs):
    time = 0
    pq = []
    job_dict = defaultdict(list)
    progressing_job = None
    completed_jobs = []

    for i in range(len(jobs)):
        requested_time, lead_time = jobs[i]
        job_dict[requested_time].append((lead_time, requested_time, i))

    print(job_dict)

    while len(completed_jobs) < len(jobs):
        if progressing_job and progressing_job[1] == time:
            completed_jobs.append(progressing_job[1] - progressing_job[0])
            progressing_job = None

        if job_dict[time]:
            for job in job_dict[time]:
                heappush(pq, job)

        while pq and not progressing_job:
            lead_time, requested_time, i = heappop(pq)
            complete_time = time + lead_time
            progressing_job = (requested_time, complete_time)

        time += 1

    return sum(completed_jobs) // len(completed_jobs)


print(solution([[0, 3], [1, 9], [3, 5]]))
