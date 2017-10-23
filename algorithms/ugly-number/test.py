#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/ugly-number/description/
## Basic Idea:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:12>
##-------------------------------------------------------------------
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        for power in [2, 3, 5]:
            while num % power == 0 and num != 0:
                num = num / power

        return num == 1
        
if __name__ == '__main__':
    s = Solution()
    print s.isUgly(1) #yes
    print s.isUgly(14) #not
    print s.isUgly(15) #yes
    print s.isUgly(16) #yes
## File: test.py ends
