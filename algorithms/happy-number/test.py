#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/happy-number/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:05:20>
##-------------------------------------------------------------------
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True

        while(n!=1):

            if (n<10):
                return False

            l = self.number_to_array(n)
            n = self.caculate_array(l)
        return True

    def caculate_array(self, l):
        ret = 0
        for n in l:
           ret += n*n
        return ret

    def number_to_array(self, n):
        l = []
        if n == 0:
            return [0]
        while (n != 0):
            l.append(n % 10)
            n = n/10

        l.reverse()
        return l

if __name__ == '__main__':
    s = Solution()
    # print s.number_to_array(19)
    print s.isHappy(19)
    print s.isHappy(7)
    print s.isHappy(2)
## File: test.py ends
