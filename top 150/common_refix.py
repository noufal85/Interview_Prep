'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

'''
#  explanation of solution
#  https://leetcode.com/problems/longest-common-prefix/discuss/6910/Python-O(n)-Solution
- prefix cant be longer than the smallest string in the list
- we take one cahr at a time from each string , and convert them to a set , if its the same lenght will be 1 
- add it to the rsult string
- if not break the loop
- return the result string
'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        res = ''
        for i in range(len(min(strs))):
            if len(set([s[i] for s in strs])) == 1:
                res += strs[0][i]
            else:
                break
        return res
    
strs = ["flower","flow","flight"]
# Output: "fl"
result = Solution().longestCommonPrefix(strs)
print(result)
strs = ["dog","racecar","car"]
# Output: ""
result = Solution().longestCommonPrefix(strs)
print(result)

strs = ["cir","car"]
# Output: "c"
result = Solution().longestCommonPrefix(strs)
print(result)
