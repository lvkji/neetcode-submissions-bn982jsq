class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList=[char for char in s]
        tList=[char for char in t]
        sList.sort()
        tList.sort()
        if sList==tList:
            return True
        else:
            return False
        