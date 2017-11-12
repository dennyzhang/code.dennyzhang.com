#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/reverse-bits/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:05:13>
##-------------------------------------------------------------------
class Solution(object):
    def reverseBits(self, n):
        i = 0
        ret = 0
        while i < 32:
            ret = ret << 1
            ret = ret | (n % 2)
            n = n >> 1
            i = i + 1
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.reverseBits(43261596)
## File: test.py ends
