class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        
        target_count = {}
        window_count = {}

        for i in range(k):
            char1 = s1[i]
            char2 = s2[i]
            target_count[char1] = target_count.get(char1, 0) + 1
            window_count[char2] = window_count.get(char2, 0) + 1
        
        if target_count == window_count:
            return True
        
        for i in range(k, len(s2)):
            entering = s2[i]
            leaving = s2[i - k]

            window_count[entering] = window_count.get(entering, 0) + 1
            window_count[leaving] -= 1

            if window_count[leaving] == 0:
                del window_count[leaving]
            
            if target_count == window_count:
                return True
        return False