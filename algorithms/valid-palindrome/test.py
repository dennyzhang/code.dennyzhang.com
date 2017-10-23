#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/valid-palindrome/description/
## Basic Idea:
## Tags: #denny-retry
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:58:07>
##-------------------------------------------------------------------
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        washed_string = []
        for ch in s:
            if (ch >='a' and ch <='z') or (ch >='A' and ch <='Z') or (ch >='0' and ch <='9'):
                washed_string.append(ch.lower())
        # print("washed_string: %s, target: %s" % (washed_string, washed_string[::-1]))
        return washed_string == washed_string[::-1]

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(".,")
    print s.isPalindrome("A man, a plan, a canal: Panama")
    print s.isPalindrome("race a car")
    print s.isPalindrome("")
    print s.isPalindrome("a.")
    print s.isPalindrome("u")
## File: test.py ends
