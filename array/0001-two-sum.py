from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, v1 in enumerate(nums):
            for i2, v2 in enumerate(nums):
                if i1 == i2:
                    continue
                elif v1 + v2 == target:
                    return [i1, i2]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, v in enumerate(nums):
            a = target - v
            if a in temp:
                return [temp[a], i]
            else:
                temp[v] = i

nums = [3,2,4]
target = 6
s = Solution()
print(s.twoSum2(nums, target))