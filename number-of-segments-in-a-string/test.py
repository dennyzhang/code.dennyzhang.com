#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/number-of-segments-in-a-string/description/
##    ,-----------
##    | Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
##    | 
##    | Please note that the string does not contain any non-printable characters.
##    | 
##    | Example:
##    | 
##    | Input: "Hello, my name is John"
##    | Output: 5
##    `-----------
##
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Idea: one pass. 2 pointer
        ## Complexity: Time O(n), Space O(1)
        res = 0
        i = 0
        while True:
            while i<len(s) and s[i] == ' ':
                i += 1

            if i>=len(s):
                break
            res += 1
            while i<len(s) and s[i] != ' ':
                i += 1
        return res
