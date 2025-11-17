class Solution:
  def dailyTemperatures(self, temperatures):
    answer = [0 for _ in range(len(temperatures))]
    stack = []

    for i, t in enumerate(temperatures):
      if stack:
        prev_t, prev_i = stack[-1]
        
        while prev_t < t:
          answer[prev_i] = i - prev_i
          stack.pop()
          
          if stack:
            prev_t, prev_i = stack[-1]
          else:
            break
      
      stack.append((t, i))

    return answer

if __name__ == '__main__':
  solution = Solution()
  print(solution.dailyTemperatures([15, 20, 25, 30]))
  print(solution.dailyTemperatures([30, 25, 20, 15]))
  print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
  print(solution.dailyTemperatures([30,60,90]))
