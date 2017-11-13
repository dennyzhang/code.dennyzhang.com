#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #todobrain
## Description:
##     https://leetcode.com/problems/factorial-trailing-zeroes/description/
##    ,-----------
##    | class Solution(object):
##    |     def trailingZeroes(self, n):
##    |         """
##    |         :type n: int
##    |         :rtype: int
##    |         """
##    |         if n < 0:
##    |             return None
##    |         if n == 0 or n == 1:
##    |             return 0
##    | 
##    |         import math
##    |         k = int(math.log(n, 5))
##    |         # print "k: %d" % (k)
##    |         res = 0
##    |         pow_val = 5
##    |         for i in xrange(1, k+1):
##    |             res += n/pow_val
##    |             pow_val *= 5
##    |         return res
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ## Idea: sqrt(num)
        ## Complexity:
        ## Sample Data:
        ##    1 2 7
        if num <= 1:
            return False
        import math
        sum = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                sum += i
                if i != num/i:
                    sum += num/i
        return sum == num
