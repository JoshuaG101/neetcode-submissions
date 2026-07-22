class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
             return False
        sMap = {}
        tMap = {}
        for l in s:
            if l in sMap:
                sMap[l] +=1
            else: sMap[l] = 1

        for l in t:
            if l in tMap:
                tMap[l] +=1
            else: tMap[l] = 1
            
        if sMap == tMap:
            return True
        else: return False
        