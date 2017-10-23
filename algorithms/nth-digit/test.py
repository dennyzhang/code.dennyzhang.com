#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/nth-digit/description/
## Basic Idea:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:14>
##-------------------------------------------------------------------
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            raise Exception("Unexpected input n: %d" % (n))

        current_digit = 0
        i = 1
        while current_digit < n:
            value_str = str(i)
            current_digit += len(value_str)
            i += 1

        if current_digit == n:
            return int(value_str[::-1][0])
        else:
            return int(value_str[::-1][current_digit - n])
            
if __name__ == '__main__':
    s = Solution()
    s.findNthDigit(3) # 3
    s.findNthDigit(4) # 4
    s.findNthDigit(11) # 0
    s.findNthDigit(12) # 1
    s.findNthDigit(13) # 1
    s.findNthDigit(15) # 2
    s.findNthDigit(17) # 3
## File: test.py ends
