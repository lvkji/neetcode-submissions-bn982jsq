class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxLength = 0
        for i in setNums:
            if i-1 not in setNums:
                length = 0
                while i+length in setNums:
                    length+=1
                maxLength = max(length,maxLength)
        return maxLength