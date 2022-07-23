"""
    @author long
    @time 2022/05/04 22:34
    @description
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        se1 = dict()
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in se1:
                return [se1[temp],i]
            se1[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,3],6))
