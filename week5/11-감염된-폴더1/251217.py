def solution(folders, p, q):
    tree = {}

    for parent, child in folders:
        tree[child] = parent

    def find_ancestors(ancestors, v):
        ancestors.append(v)

        if v == 'root':
            return ancestors

        return find_ancestors(ancestors, tree[v])

    p_ancestors = find_ancestors([], p)
    q_ancestors = find_ancestors([], q)

    p_set = set(p_ancestors)

    for q_parent in q_ancestors:
        if q_parent in p_set:
            return q_parent


print(solution([['root', 'b'], ['root', 'c'], ['b', 'd'], ['b', 'e'], ['e', 'f']], 'd', 'e'))  # 'b'
print(solution([['root', 'b'], ['root', 'c'], ['b', 'd'], ['b', 'e'], ['e', 'f']], 'b', 'e'))  # 'b'
print(solution([['root', 'b'], ['root', 'c'], ['b', 'd'], ['b', 'e'], ['e', 'f']], 'c', 'e'))  # 'root'
