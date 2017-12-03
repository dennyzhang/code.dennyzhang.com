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
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ## Basic Idea:
        ## Complexity: Time O(n), Space O(1)
        ## Assumptions:
        length = len(s)
        l = list(s)
        should_reverse = True
        i = 0
        while i < length:
            if i+k-1 < length:
                j = i+k-1
            else:
                j = length - 1

            if should_reverse:
                # print("i: %d, j: %d" % (i, j))
                start = i
                end = j
                while start < end:
                    l[start],l[end] = l[end], l[start]
                    start += 1
                    end -= 1
            should_reverse = not should_reverse
            i = j + 1
        return ''.join(l)
