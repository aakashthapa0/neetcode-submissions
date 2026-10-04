class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound():
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def upper_bound():
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return right
        
        first = lower_bound()
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        
        last = upper_bound() - 1
        return [first, last]