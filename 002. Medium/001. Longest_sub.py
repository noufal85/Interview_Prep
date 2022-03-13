#Longest Substring Without Repeating Characters

from tkinter import S


def is_unique(string):
    return len(set(string)) == len(string)


def longest_sub_complex(string):
    start = 0 
    end = len(string)
    max_len = 0

    for i in range(start,end+1):
        for j in range(i+1, end+1):
            #print(string[i:j])
            if is_unique(string[i:j]):
                max_len = max(max_len, j-i)

    return max_len

def lengthOfLongestSubstring(s: str) -> int:
    chars = [0] * 128

    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]
        chars[ord(r)] += 1
        while chars[ord(r)] > 1:
            #print('second')
            l = s[left]
            chars[ord(l)] -= 1
            left += 1
        res = max(res, right - left + 1)
        #print('length now is: ', res)
        right += 1
    return res

def leng_substr_fast(s):
    n = len(s)
    ans = 0
    map = {}
    i = 0

    for j in range(n):
        if s[j] in map:
            i = max(map[s[j]], i)

        ans = max(ans,j-i+1)
        print(ans)
        map[s[j]] = j+1
        print(map)

    return ans


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        map = {}
        max_l = 0
        i = 0
        
        for j in range(l):
            if s[j] in map:
                i = max(map[s[j]], i)
            print(type(i))   
            print(type(max_l) )
            print(max_l, i)
            max_l = max(max_l,(j-i)+1)
            map[s[j]] = j+1
        return max_l
            
        





if __name__ ==  "__main__":
   #print(lengthOfLongestSubstring('abcdefaghijl')) 
    # print(longest_sub_complex('bbbbb'))
    # print(longest_sub_complex('pwwkew'))
    # print(longest_sub_complex('abcdeaf'))
    print(leng_substr_fast('abcdefaxyfz'))

    #print(Solution.lengthOfLongestSubstring(s='abcdefg'))
    s= Solution()
    print(s.lengthOfLongestSubstring(s= 'abcabcbb'))
