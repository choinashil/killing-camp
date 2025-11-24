from heapq import heappop, heappush


def dijkstra(graph, start, end):
    INF = float('inf')

    weights = {v: INF for v in graph}
    weights[start] = 0

    pq = []
    heappush(pq, (0, start))

    while pq:
        cur_w, cur_v = heappop(pq)

        if weights[cur_v] < cur_w:
            continue

        for next_v, w in graph[cur_v]:
            next_w = weights[cur_v] + w

            if next_w < weights[next_v]:
                weights[next_v] = next_w
                heappush(pq, (next_w, next_v))

    return weights[end]


graph = {
    'A': [('B', 4), ('C', 2), ('D', 5)],
    'B': [('D', 3)],
    'C': [],
    'D': []
}
print(dijkstra(graph, 'A', 'D'))
