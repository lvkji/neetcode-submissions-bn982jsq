class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*(len(nums)) #Resulting output array
        prefix = 1 #Initialize first prefix value to 1
        for i in range(len(nums)):
            res[i] = prefix #Take prefix and put it in position i
            prefix*=nums[i] #Prefix multiplied by array value
        postfix=1 #INitialize postfix value to 1
        #Begin at the end of the input array for the postfix (enter values backwards)
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix #Multiply prefix and postfix together
            postfix*=nums[i] #Update the postfix value with whatever is in nums
        return res #Return the resulting array