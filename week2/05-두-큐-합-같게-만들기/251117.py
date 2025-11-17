def solution(queue1, queue2):
    answer = -1
		
    # 두 큐를 연결한다.
    queue = queue1 + queue2

		# queue1의 초기 합을 기록한다.
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)

		# queue1의 목표값을 두 큐의 전체 합의 절반으로 설정한다.
    target = (q1_sum + q2_sum) / 2

		# 두 포인터의 시작값을 설정한다.
    i, j = 0, len(queue1)
		
    for answer in range(0, 3 * len(queue1)):
				# queue1의 합이 목표값보다 큰 경우
        if q1_sum > target:
						# queue1의 원소를 pop하고 큐의 합에 반영한다.
            q1_sum -= queue[i]
						# 포인터를 이동시킨다.
            i += 1
        elif target > q1_sum:
						# queue1에 원소를 insert하고 큐의 합에 반영한다.
            q1_sum += queue[j]
						# 포인터를 이동시킨다.
            j += 1
				# queue1의 합이 목표값과 같은 경우 정답을 반환한다.
        else:
            return answer
				
        # 두 포인터가 만나거나 범위를 벗어난 경우 -1을 반환한다.
        if (i == j) or (j == len(queue)):
            return -1

def solution(queue1, queue2):
    queue = queue1 + queue2 
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    target = (q1_sum + q2_sum) / 2

    i, j = 0, len(queue1)

    for answer in range(0, 3 * len(queue1)):
        if (i == j) or (j == len(queue)):
            return -1
        
        if q1_sum > target:
            q1_sum = q1_sum - queue[i]
            i += 1
        elif q1_sum < target:
            q1_sum = q1_sum + queue[j]
            j += 1
        else:
            return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
