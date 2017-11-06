#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/longest-palindrome/description/
##    ,-----------
##    | Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
##    | 
##    | This is case sensitive, for example "Aa" is not considered a palindrome here.
##    | 
##    | Note:
##    | Assume the length of given string will not exceed 1,010.
##    | 
##    | Example:
##    | 
##    | Input:
##    | "abccccdd"
##    | 
##    | Output:
##    | 7
##    | 
##    | Explanation:
##    | One longest palindrome that can be built is "dccaccd", whose length is 7.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-03 10:14:57>
##-------------------------------------------------------------------
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Idea: Use a map and count characters
        ## Complexity:
        count_map = {}
        for ch in s:
            if count_map.has_key(ch) is False:
                count_map[ch] = 1
            else:
                count_map[ch] += 1
        has_odd = False
        res = 0
        for ch in count_map.keys():
            if count_map[ch] % 2 == 0:
                res += count_map[ch]
            else:
                has_odd = True
                res += count_map[ch] - 1
        return res+1 if has_odd else res
