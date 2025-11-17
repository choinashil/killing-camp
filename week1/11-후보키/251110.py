def solution(relation):
	def create_subsets(curr, start):
		all_subsets.append(curr[:])
		
		for i in range(start, col_len):
				curr.append(i)
				create_subsets(curr, i + 1)
				curr.pop()

	def is_unique(subset):
		if len(subset) == 0:
			return False
		
		s = set()

		for r in range(row_len):
			key = ''.join(relation[r][c] for c in subset)
			
			if key in s:
				return False
			s.add(key)
		
		return True
	
	def is_minimal(subset, candidate_keys):
		for candidate_key in candidate_keys:
			if set(candidate_key).issubset(set(subset)):
				return False
			
		return True

	row_len = len(relation)
	col_len = len(relation[0])
	
	# 1. 모든 부분집합 생성
	all_subsets = []
	create_subsets([], 0)

	# 2. 유일성 필터링
	unique_keys = [subset for subset in all_subsets if is_unique(subset)]
	unique_keys.sort(key=len)

	# 3. 최소성 필터링
	candidate_keys = []
	for key in unique_keys:
			if is_minimal(key, candidate_keys):
					candidate_keys.append(key)      

	return len(candidate_keys)

print(solution([
	["100","ryan","music","2"],
	["200","apeach","math","2"],
	["300","tube","computer","3"],
	["400","con","computer","4"],
	["500","muzi","music","3"],
	["600","apeach","music","2"]
]))
