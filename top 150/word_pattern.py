'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(set(pattern)) != len(set(s.split())):
            print('set(pattern): ', set(pattern))
            return False
        if len(pattern) != len(s.split()):
            return False
        d = {}
        for i in range(len(pattern)):
            print(f'pattern[i]: {pattern[i]}, d-pair: {d}')
            if pattern[i] not in d:
                d[pattern[i]] = s.split()[i]
            elif d[pattern[i]] != s.split()[i]:
                return False
            # print('d: ', d)
            
        return True
    
pattern = "abba"
s = "dog cat cat dog"
# Output: true
result = Solution().wordPattern(pattern, s)
print(result)
pattern= "aba"
s= "cat cat cat dog"
# Output: false
result = Solution().wordPattern(pattern, s)
print(result)
        