#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description :
##     https://leetcode.com/problems/binary-number-with-alternating-bits/description/
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-21 23:37:09>
##-------------------------------------------------------------------
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n == 1:
            return True

        last_digit = None
        while n != 0:
            if last_digit is None:
                last_digit = n % 2
            else:
                if last_digit + (n % 2) != 1:
                    return False
                last_digit = n % 2
            n = n / 2
        return True

if __name__ == '__main__':
    s = Solution()
    print s.hasAlternatingBits(5)
    print s.hasAlternatingBits(3)
    print s.hasAlternatingBits(7)
    print s.hasAlternatingBits(11)
    print s.hasAlternatingBits(10)
## File: test.py ends
