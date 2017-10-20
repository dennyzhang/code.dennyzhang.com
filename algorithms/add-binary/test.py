#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description :
##     https://leetcode.com/problems/add-binary/description/
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-20 15:35:38>
##-------------------------------------------------------------------
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

if __name__ == '__main__':
    s = Solution()
    print s.addBinary("11", "1") # 100
    print s.addBinary("0", "0") # 0
    print s.addBinary("101", "0") # 101
    print s.addBinary("101", "101") # 1010
## File: test.py ends
