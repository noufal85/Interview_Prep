'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
'''
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy apprach - https://youtu.be/9kyHYVxL4fw?t=497
        jumps = 0
        destination = len(nums)-1
        coverage = 0
        last_jump_index = 0
        for i in range(destination):
            coverage = max(coverage, i+nums[i])
            if i == last_jump_index:
                jumps += 1
                last_jump_index = coverage
                if coverage >= destination:
                    break
        return jumps
    
nums = [2,3,1,1,4]
result = Solution().jump(nums)
print(result)
nums = [2,3,0,1,4]
result = Solution().jump(nums)
print(result)

        
        