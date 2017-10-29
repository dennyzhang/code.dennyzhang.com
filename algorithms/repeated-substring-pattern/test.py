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
##     https://leetcode.com/problems/repeated-substring-pattern/description/
##    ,-----------
##    | Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
##    | 
##    | Example 1:
##    | Input: "abab"
##    | 
##    | Output: True
##    | 
##    | Explanation: It's the substring "ab" twice.
##    | Example 2:
##    | Input: "aba"
##    | 
##    | Output: False
##    | Example 3:
##    | Input: "abcabcabcabc"
##    | 
##    | Output: True
##    | 
##    | Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-27 11:24:41>
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
