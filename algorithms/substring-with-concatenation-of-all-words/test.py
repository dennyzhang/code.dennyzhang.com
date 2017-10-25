#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
##    ,-----------
##    | You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
##    | 
##    | For example, given:
##    | s: "barfoothefoobarman"
##    | words: ["foo", "bar"]
##    | 
##    | You should return the indices: [0,9].
##    | (order does not matter).
##    `-----------
##
##    
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ## Basic Idea:
        ## Complexity:
        ## barfoothefoobarman -> bar foo the foo bar man

if __name__ == '__main__':
    s = Solution()
    # print s.findSubstring("barfoothefoobarman")
## File: test.py ends
