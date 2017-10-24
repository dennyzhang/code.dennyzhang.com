#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/array-partition-i/description/
##    ,-----------
##    | Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
##    | 
##    | Example 1:
##    | Input: [1,4,3,2]
##    | 
##    | Output: 4
##    | Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
##    | Note:
##    | n is a positive integer, which is in the range of [1, 10000].
##    | All the integers in the array will be in the range of [-10000, 10000].
##    `-----------
##
## Basic Idea:
## Complexity:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:07>
##-------------------------------------------------------------------
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        sorted_nums = sorted(nums)
        i = 0
        while i < len(sorted_nums)/2:
            ret = ret + sorted_nums[i*2]
            i = i + 1
        return ret
            
if __name__ == '__main__':
    s = Solution()
    print s.arrayPairSum([1,4,3,2]) # 4
    print s.arrayPairSum([1,2,3,4,5, 6]) # 9
## File: test.py ends
