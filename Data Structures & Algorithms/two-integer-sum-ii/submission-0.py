class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Given a sorted array nums return indices of two values in nums such that they add up to target
        left=0
        right=len(numbers)-1
        while left < right:
            current_sum = numbers[left]+numbers[right]
            if current_sum == target:
                return [left+1,right+1]
            elif current_sum < target:
                left+=1
            elif current_sum > target:
                right-=1