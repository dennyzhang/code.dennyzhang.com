#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/sum-of-two-integers/description/
## Basic Idea:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 13:19:41>
##-------------------------------------------------------------------
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        list1 = []
        list2 = []

        if a == 0:
            list1 = [0]

        if b == 0:
            list2 = [0]
        
        while a != 0:
            list1.append(a%2)
            a = a/2

        while b != 0:
            list2.append(b%2)
            b = b/2

        i = 0
        j = 0

        val = 0
        has_overflow = False
        while i < len(list1) and j < len(list2):
            if list1[i] == 0 and list2[j] == 0:
                if has_overflow is True:
                    val = (val >> 1) | 1
                    has_overflow = False
                else:
                    val = (val >> 1) | 0

            if list1[i] == 0 and list2[j] == 1:
                if has_overflow is True:
                    val = (val >> 1) | 0
                    has_overflow = True
                else:
                    val = (val >> 1) | 0

            if list1[i] == 1 and list2[j] == 0:
                val = (val >> 1) | 1

            if list1[i] == 1 and list2[j] == 1:
                val = (val >> 1) | 0
                has_overflow = True

        print list1
        print list2

if __name__ == '__main__':
    s = Solution()
    print s.getSum(1, 2)
    print s.getSum(2, 2)
    print s.getSum(0, 2)
    print s.getSum(0, 0)
    print s.getSum(5, 22)
    # print s.getSum(-2, 3)
## File: test.py ends
