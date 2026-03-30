class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2= ''.join([char for char in s if char.isalnum()])
        reverseds=s2[::-1]
        if s2.lower() == reverseds.lower():
            return True
        else:
            return False