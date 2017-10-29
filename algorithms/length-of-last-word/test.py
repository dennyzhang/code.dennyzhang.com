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
##     https://leetcode.com/problems/length-of-last-word/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:18>
##-------------------------------------------------------------------
class Solution(object):
    # def lengthOfLastWord(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     s = s.strip(" ")
    #     word_list = s.split(" ")
    #     return len(word_list[-1])

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(-(len(s)-1), 0):
        
if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLastWord("a ")
    print s.lengthOfLastWord("hello world")
    print s.lengthOfLastWord("hello")
    print s.lengthOfLastWord("")
## File: test.py ends
