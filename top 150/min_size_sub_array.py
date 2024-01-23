'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        min_len = len(nums)+1
        total = 0
        while right < len(nums):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        return min_len if min_len <= len(nums) else 0
        
        