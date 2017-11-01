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
##     https://leetcode.com/problems/implement-strstr/description/
##    ,-----------
##    | Implement strStr().
##    | 
##    | Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:19>
##-------------------------------------------------------------------
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ## Idea:
        ## Complexity: Time O(n*k), Space O(1)
        ##    hello, hello
        ##       lo
        h_length = len(haystack)
        n_length = len(needle)
        if n_length == 0:
            return 0

        for i in range(0, h_length-n_length+1):
            if haystack[i:(i+n_length)] == needle:
                return i
        return -1