class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        best = 0
        freq = {}
        for i in range(len(fruits)):
            fruit = fruits[i]
            freq[fruit] = freq.get(fruit, 0) + 1

            while len(freq) > 2:
                leaving = fruits[left]
                freq[leaving] -= 1
                if freq[leaving] == 0:
                    del freq[leaving]
                left += 1
            best = max(best, i - left + 1)
        return best