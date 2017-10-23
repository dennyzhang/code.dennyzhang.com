#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description :
##     https://leetcode.com/problems/nth-digit/description/
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-22 23:41:37>
##-------------------------------------------------------------------
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        current_digit = 0
        i = 1
        while current_digit < n:
            current_digit += len(str(i))
            i += 1

        if current_digit == n:
            return i
        else:
            value_str = str(i)
            return value_str[...]
            
if __name__ == '__main__':
    s = Solution()
    print s.findNthDigit(3)
    print s.findNthDigit(4)
    print s.findNthDigit(11)
## File: test.py ends
