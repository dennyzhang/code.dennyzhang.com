#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #todobrain
## Description:
##      https://leetcode.com/problems/single-number/description/
## ,-----------
## | Given an array of integers, every element appears twice except for one. Find that single one.
## | 
## | Note:
## | Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
## `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:03>
##-------------------------------------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in nums:
            x = x ^ i
        return x

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1, 2, 1])
    print s.singleNumber([2, 2, 1])
## File: test.py ends
