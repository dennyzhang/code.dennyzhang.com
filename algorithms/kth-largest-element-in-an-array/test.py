#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/kth-largest-element-in-an-array/description/
## Basic Idea: insert sort: maintain array with k items
## Complexity: Time: O(n)*O(k)
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:34:47>
##-------------------------------------------------------------------
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_list = [None]*k
        for num in nums:
            # find where to insert
            insert_index = -1
            for i in range(0, k):
                max_value = max_list[i]
                if max_value is None:
                    insert_index = i
                    break
                elif max_value == num:
                    insert_index = i
                    break
                elif max_value < num:
                    insert_index = i
                    break
            # insert
            if insert_index != -1:
                for i in range(k-1, insert_index, -1):
                    max_list[i] = max_list[i-1]
                max_list[insert_index] = num
        # Get the value
        return max_list[k-1]
                
if __name__ == '__main__':
    s = Solution()
    print s.findKthLargest([3,2,1,5,6,4], 2)
## File: test.py ends
