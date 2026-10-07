class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + speed - 1) // speed
                if total_hours > h:
                    return False
            return True
        
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return left