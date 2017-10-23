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
