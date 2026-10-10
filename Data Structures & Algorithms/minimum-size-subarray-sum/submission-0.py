class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        best = len(nums) + 1

        for i in range(len(nums)):
            window_sum += nums[i]

            while window_sum >= target:
                best = min(best, i - left + 1)
                window_sum -= nums[left]
                left += 1
            
        return 0 if best == len(nums) + 1 else best