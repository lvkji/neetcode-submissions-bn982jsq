class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i]+=1
        for j in count:
            if count[j] > 1:
                return j
        