#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description :
##      https://leetcode.com/problems/single-number/description/
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-17 20:39:11>
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
