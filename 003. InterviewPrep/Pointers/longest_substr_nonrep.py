def lengthOfLongestSubstring(s):
    seen = {}
    l = 0
    output = 0
    for c in range(len(s)):
        if s[c] not in seen:
            output = max(output, c-l+1)
        
        else:
            if seen[s[c]] < l:
                output = max(output, c-l+1)
            else:
                l = seen[s[c]] + 1
        seen[s[c]] = c
    
    return output

def lengthOfLongestSubstring2(s):
    l = len(s)
    map = {}
    max_l = 0
    i = 0

    for j in range(l):
        if s[j] in map:
            i = max(map[s[j]], i)

            max_l = max(max_l,(j-i)+1)
            map[s[j]] = j+1

    return max_l
