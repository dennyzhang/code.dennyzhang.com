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
##     https://leetcode.com/problems/perfect-number/description/
##    ,-----------
##    | We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
##    | 
##    | Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
##    | Example:
##    | Input: 28
##    | Output: True
##    | Explanation: 28 = 1 + 2 + 4 + 7 + 14
##    | Note: The input number n will not exceed 100,000,000. (1e8)
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
