class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Frequency Counter Hashmap Comparison
        countS = {}
        for i in s:
            if i not in countS:
                countS[i] = 0
            countS[i]+=1
        countT = {}
        for j in t:
            if j not in countT:
                countT[j] = 0
            countT[j]+=1
        #If key,value pairs are the same strings must be anagrams
        if countS == countT:
            return True
        else:
            return False
