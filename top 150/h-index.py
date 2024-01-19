'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
'''
from typing import List
#  brute force 
class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1 and citations[0] == 0:
            return 0
        if len(citations) == 1 and citations[0] > 0:
            return 1
        citationh = 0
        for i in citations:
            # print(f'i is {i}')
            sum = 0
            for citation in citations:
                # print(citation)
                if citation - i >= 0:
                    sum += 1
            if sum >= i:
                citationh = max(citationh,i)
                # print(f'assigned citationh to {citationh}')
        return citationh

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        print(citations)
        citationh = 0
        for i in range(len(citations)):
            if citations[i] >= len(citations)-i:
                citationh = max(citationh,len(citations)-i)
        return citationh
                   
    

citations = [3,0,6,1,5]
result = Solution().hIndex(citations)
print(result)
citations = [1,3,1]
result = Solution().hIndex(citations)
print(result)
citations = [0,1]
result = Solution().hIndex(citations)
print(result)
            
                     