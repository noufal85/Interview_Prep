'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

from typing import List
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # https://www.youtube.com/watch?v=bNvIQI2wAjk&ab_channel=NeetCode
        #  build prefix
        res = [1] * len(nums)
        prefix =1
        for i in range(len(nums)):            
            res[i] = prefix
            prefix *= nums[i]
            # print(i,prefix,res)
        # build suffix
        print(res)
        suffix = 1
        for i in range(len(nums)-1,-1,-1):            
            res[i] *= suffix
            suffix *= nums[i]
            # print(i,suffix,res)
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        #  left pass
        for i in range(1,n):
            result[i] = result[i-1]*nums[i-1]
        print(result)
        # right pass
        for i in range(n-2,-1,-1):
            result[i] *= nums[i+1]
            nums[i] *= nums[i+1]
        return result
        
        
    
nums = [1,2,3,4]
result = Solution().productExceptSelf(nums)
print(result)
nums = [-1,1,0,-3,3]
result = Solution().productExceptSelf(nums)
print(result)

            

      