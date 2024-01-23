'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        # return True
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False
        return True
    
s = "egg"
t = "add"
# Output: true
result = Solution().isIsomorphic(s, t)
print(result)

s = "foo"
t = "bar"
# Output: false
result = Solution().isIsomorphic(s, t)
print(result)

s = "paper"
t = "title"
# Output: true
result = Solution().isIsomorphic(s, t)
print(result)
        
        
