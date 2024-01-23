'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
from typing import List
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0
        while right < len(s):
            if s[right] not in s[left:right]:
                max_len = max(max_len, right- left +1)
                right += 1
            else:
                while s[right] in s[left:right] and right:
                    left += 1
        return max_len
#  complexity of this solution is O(n^2)
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = result = 0
        seen = {}
        for i , char in enumerate(s):
            if char in seen and start <= seen[char]:
                start = seen[char] + 1
            else:
                result = max(result, i-start+1)
            seen[char] = i
        return result
    
#  complexity of this solution is O(n)
