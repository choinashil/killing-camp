from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for str in strs:
            sorted_str = ''.join(sorted(str))
            anagrams[sorted_str].append(str)

        return list(anagrams.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams(['']))
    print(solution.groupAnagrams(['a']))
