#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/number-complement/description/
## Basic Idea:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 13:19:41>
##-------------------------------------------------------------------
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = num
        ret = 0
        digit_count = 0

        while i != 0:
            reverse_current_digit = 1 ^ (i % 2)
            ret = (reverse_current_digit << digit_count) | ret
            digit_count = digit_count + 1
            i = i >> 1
            # print("i: %i, ret: %d, digit_count: %d, reverse_current_digit: %d", i, ret, digit_count, reverse_current_digit)

        return ret
if __name__ == '__main__':
    s = Solution()
    print s.findComplement(5) # 2
    print s.findComplement(3) # 0
    print s.findComplement(1) # 0
## File: test.py ends
