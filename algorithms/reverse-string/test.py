#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/reverse-string/description/
## Basic Idea:
## Complexity:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:04>
##-------------------------------------------------------------------
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

if __name__ == '__main__':
    s = Solution()
    print s.reverseString("hello")
    print s.reverseString("denny")
## File: test.py ends
