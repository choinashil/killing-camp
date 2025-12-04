from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict = {id: i for i, id in enumerate(id_list)}
    blacklist = defaultdict(set)

    for r in report:
        fr, to = r.split(' ')
        blacklist[to].add(fr)

    for key in blacklist:
        if len(blacklist[key]) >= k:
            for p in blacklist[key]:
                answer[id_dict[p]] += 1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))  # [2, 1, 1, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))  # [0, 0]
