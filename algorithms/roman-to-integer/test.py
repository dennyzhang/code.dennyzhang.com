#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/roman-to-integer/description/
## Basic Idea:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:13>
##-------------------------------------------------------------------
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        i = 0
        j = 0
        for ch in s:
            ret += roman_dict[ch]
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt("MCMXCVI") # 1996
    print s.romanToInt("III")
    print s.romanToInt("VIII")    
    print s.romanToInt("X")
    print s.romanToInt("M")
    print s.romanToInt("MM")
## File: test.py ends
