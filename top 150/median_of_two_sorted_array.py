'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
 
'''

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_array = []
        i = 0
        j = 0
        len1 = len(nums1)
        len2 = len(nums2)
        while i <= len1-1 and j <= len2-1:            
            if nums1[i] < nums2[j]:
                new_array.append(nums1[i])
                i = i+1
            else:
                new_array.append(nums2[j])
                j = j+1
        print(len1,len2,new_array,i,j)
        if i < len1:
            new_array.extend(nums1[i:])
        if j < len2:
            new_array.extend(nums2[j:])

        print(new_array)
      
    
nums1 = [1,3]
nums2 = [4]
result = Solution().findMedianSortedArrays(nums1, nums2)
        