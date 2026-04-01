class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window Algorithm using Set
        charSet = set()
        left = 0
        longest = 0
        for right in range(len(s)):
            # Duplicate exists in the window
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            # Add right values to the window
            charSet.add(s[right])
            longest = max(longest, right-left+1)
        return longest