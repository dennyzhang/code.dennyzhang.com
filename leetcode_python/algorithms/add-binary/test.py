#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/add-binary/description/
##    ,-----------
##    | Given two binary strings, return their sum (also a binary string).
##    | 
##    | For example,
##    | a = "11"
##    | b = "1"
##    | Return "100".
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:07>
##-------------------------------------------------------------------
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        val1 = 0
        for ch in a:
            val1 = val1 << 1
            if ch == '1':
                val1 = val1 + 1
            else:
                if ch != '0':
                    raise Exception("Invalid output")

        val2 = 0
        for ch in b:
            val2 = val2 << 1
            if ch == '1':
                val2 = val2 + 1
            else:
                if ch != '0':
                    raise Exception("Invalid output")

        # print("val1: %s, val2: %s" % (val1, val2))
        l = []
        val = val1 + val2
        if val == 0:
            return "0"
        else:
            while val != 0:
                l.append(str(val % 2))
                val = val >> 1
            l.reverse()
            return "".join(l)

if __name__ == '__main__':
    s = Solution()
    print s.addBinary("11", "1") # 100
    print s.addBinary("0", "0") # 0
    print s.addBinary("101", "0") # 101
    print s.addBinary("101", "101") # 1010
## File: test.py ends
