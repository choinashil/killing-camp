from collections import defaultdict

def solution(info, edges):
    graph = defaultdict(set)
    for parent, child in edges:
        graph[parent].add(child)

    def dfs(cur_v, sheep, wolf, can_visit):
        nonlocal answer

        # 현재 노드 처리 (양/늑대 카운트)
        if info[cur_v]:
            wolf += 1
        else:
            sheep += 1

        
        # 늑대가 양과 같거나 많으면 return
        if wolf >= sheep:
            return
        
        answer = max(answer, sheep)
        
        # 다음으로 방문할 곳 추가
        # 방법1
        for child in graph[cur_v]:
            can_visit.add(child)

        # 방법2 (차집합)
        # can_visit = can_visit | set(graph[cur_v])

        for next_v in can_visit:
            # can_visit 은 원본을 전달하지 않게 주의
            dfs(next_v, sheep, wolf, can_visit - {next_v})

    answer = 0
    dfs(0, 0, 0, set())
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
