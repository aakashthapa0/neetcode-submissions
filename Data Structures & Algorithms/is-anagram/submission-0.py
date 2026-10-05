class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for each in s:
            count[each] = count.get(each, 0) + 1
        
        for each in t:
            if each not in count or count[each] == 0:
                return False
            count[each] -= 1
        return True
