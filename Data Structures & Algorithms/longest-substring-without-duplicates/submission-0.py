class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        freq = {}

        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1

            while freq[char] > 1:
                leaving = s[left]
                freq[leaving] -= 1
                left += 1
            
            best = max(best, right - left + 1)
        return best