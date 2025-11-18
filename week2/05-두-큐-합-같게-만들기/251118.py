def solution(queue1, queue2):
    q = queue1 + queue2

    q1_sum = sum(queue1)
    q2_sum = sum(queue2)

    target = (q1_sum + q2_sum) / 2

    l, r = 0, len(queue1)

    for i in range(3 * len(q)):
        if l == r or r == len(q):
            return - 1

        if q1_sum > target:
            q1_sum -= q[l]
            l += 1
        elif q1_sum < target:
            q1_sum += q[r]
            r += 1
        else:
            return i

    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))  # 7
print(solution([1, 1], [1, 5]))  # -1
