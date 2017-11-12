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
##     https://leetcode.com/problems/palindrome-number/description/
##    ,-----------
##    | Determine whether an integer is a palindrome. Do this without extra space.
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:59:15>
##-------------------------------------------------------------------
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        val = x
        y = 0
        while val != 0:
            y = 10*y + (val%10)
            val = val / 10
        # print("x: %d, y: %d" % (x, y))
        return x == y

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(121)
    print s.isPalindrome(123)
    print s.isPalindrome(3)
    print s.isPalindrome(43)
## File: test.py ends
