#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/hamming-distance/description/
## Basic Idea:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:15>
##-------------------------------------------------------------------
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        while x != 0 or y != 0:
            if (x % 2) != (y % 2):
                count = count + 1
            x = x >> 1
            y = y >> 1
        return count
        
if __name__ == '__main__':
    s = Solution()
    print s.hammingDistance(1, 4) # 2
    print s.hammingDistance(2, 10) # 1
## File: test.py ends
