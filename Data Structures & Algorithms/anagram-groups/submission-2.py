class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Group anagrams into lists based off sorted values
        result = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            result[sortedS].append(s)
        return list(result.values())
        # Time Complexity: O(m*nlogn)
        # Space Complexity: O(m*n)