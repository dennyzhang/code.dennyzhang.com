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
##     https://leetcode.com/problems/power-of-four/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2018-01-08 09:22:36>
##-------------------------------------------------------------------
class Solution(object):
    def isPowerOfFour(self, num):
        return ((num - 1) & num == 0 and (num-1) % 3 == 0)

    def isPowerOfFour_2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        if num == 1:
            return True

        # 0101 0101 0101 ... 0101 0100
        const_val = 0

        for i in range(1, 8):
            const_val = const_val << 4
            const_val = const_val | 5

        const_val = const_val << 4
        const_val = const_val | 4
        # print const_val

        return ((num - 1) & num == 0) and (num & const_val == num)
    # # with loop
    # def isPowerOfFour(self, num):
    #     """
    #     :type num: int
    #     :rtype: bool
    #     """
    #     if num == 0:
    #         return False
    #     while num % 4 == 0:
    #         num = num/4
    #     return (num == 1)

if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfFour(1) # True
    print s.isPowerOfFour(2)
    print s.isPowerOfFour(16) # True
    print s.isPowerOfFour(32)
    print s.isPowerOfFour(0)
    print s.isPowerOfFour(5)
    print s.isPowerOfFour(268435456) # True
## File: test.py ends
