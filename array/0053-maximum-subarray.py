from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum = 0
        for v in nums:
            if sum > 0:
                sum += v
            else:
                sum = v
            ans = max(ans, sum)
        return ans

    def maxSubArray2(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            # print(nums)
        return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))