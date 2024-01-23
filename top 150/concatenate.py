#  30. Substring with Concatenation of All Words
'''
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
We return an empty array.
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
'''
from typing import List
import copy
class Solution2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        if not words: return result
        word_len = len(words[0])
        list_len = len(words)
        total_words_len = list_len*word_len
        for i in range(len(s)-total_words_len+1):
            sub_len = s[i:i+total_words_len]
            print(sub_len)
            seen =[]
            copy_words = copy.copy(words) 
            for j in range(list_len):
                sub_len2 = sub_len[j*word_len:(j+1)*word_len]
                # print(sub_len2)
                # make a copy of words
                         #  
                for k, word__ in enumerate(copy_words):
                    if sub_len2 == word__:
                        copy_words.pop(k)
                        break
            print(copy_words)
            if not copy_words:
                result.append(i)
                # print(f'{i}-#################################-full match')
                
                        
        return result
#  complexity of this solution is O(n^2)

from typing import List
import copy
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass