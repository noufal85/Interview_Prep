'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        seen = 0
        for i in range(len(t)):
            if t[i] == s[seen]:
                seen += 1
            if seen == len(s):
                return True
        return False
    

s = "abc"
t = "ahbgdc"
# Output: true
result = Solution().isSubsequence(s, t)
print(result)
s = "axc"
t = "ahbgdc"
# Output: false
result = Solution().isSubsequence(s, t)
print(result)

        