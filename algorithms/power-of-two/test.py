#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/power-of-two/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:15>
##-------------------------------------------------------------------
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n < 0:
        #     return False

        # while n % 2 == 0 and n != 0:
        #     n = n/2
        # return n == 1

        if n <= 0:
            return False
        return n & (n-1) == 0

if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfTwo(4) # True
    print s.isPowerOfTwo(15) # False
    print s.isPowerOfTwo(16) # True
    print s.isPowerOfTwo(-1) # False
## File: test.py ends
