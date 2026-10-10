class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0
        for i in range(k):
            if blocks[i] == "W":
                white_count += 1
        
        best = white_count
        for right in range(k, len(blocks)):
            if blocks[right] == "W":
                white_count += 1

            if blocks[right - k] == "W":
                white_count -= 1
            
            best = min(best, white_count)
        return best