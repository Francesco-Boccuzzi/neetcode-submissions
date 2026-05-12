class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        n = len(s)
        if n != len(t):
            return False
        for char in s:
            if char in sMap.keys():
                sMap[char] += 1
            else:
                sMap[char] = 1
        for char in t:
            if char in tMap.keys():
                tMap[char] += 1
            else:
                tMap[char] = 1
        for char in sMap.keys():
            if char not in tMap.keys() or sMap[char] != tMap[char]:
                return False
        return True
            
