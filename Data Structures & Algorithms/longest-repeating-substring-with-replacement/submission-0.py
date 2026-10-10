class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        best = 0
        freq = {}

        for i in range(len(s)):
            char = s[i]
            freq[char] = freq.get(char, 0) + 1

            window_length = i - left + 1
            max_freq = max(freq.values())
            
            while window_length - max_freq > k:
                leaving = s[left]
                freq[leaving] -= 1

                if freq[leaving] == 0:
                    del freq[leaving]
                
                left += 1
                window_length = i - left + 1
                max_freq = max(freq.values())
            best = max(best, i - left + 1)
        return best