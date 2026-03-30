class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        longest = 0
        for i in set_nums:
            length = 0 #Reset the length at the start of a new value
            if (i-1) not in set_nums: #Start of a sequence if i does not have left neighbor
                while (i+length) in set_nums: #While next value in set add 1 to length
                    length+=1
                longest=max(length,longest)
        return longest
            