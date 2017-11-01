#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags:
## Description:
##     https://leetcode.com/problems/reverse-string-ii/description/
##    ,-----------
##    | Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
##    | Example:
##    | Input: s = "abcdefg", k = 2
##    | Output: "bacdfeg"
##    | Restrictions:
##    | The string consists of lower English letters only.
##    | Length of the given string and k will in the range [1, 10000]
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:14>
##-------------------------------------------------------------------
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Basic Idea:
        ## Complexity:

if __name__ == '__main__':
    s = Solution()
    # print s.romanToInt("MCMXCVI")
