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
##     https://leetcode.com/problems/reverse-words-in-a-string/description/
##    ,-----------
##    | Given an input string, reverse the string word by word.
##    | 
##    | For example,
##    | Given s = "the sky is blue",
##    | return "blue is sky the".
##    | 
##    | Update (2015-02-12):
##    | For C programmers: Try to solve it in-place in O(1) space.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-26 21:41:00>
##-------------------------------------------------------------------
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## Basic Idea:
        ## the sky is blue
        ## eulb si yks eht
        ## blue is sky the
        ## Complexity: Time O(n), Space O(1)
        # reverse
        s = s[::-1]
        res = []
        for item in s.split(" "):
            if item == "":
                continue
            res.append(item[::-1])
        return ' '.join(res)
