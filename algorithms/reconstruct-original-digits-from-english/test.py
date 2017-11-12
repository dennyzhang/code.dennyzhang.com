#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #todobrain, #redo
## Description:
##     https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
##    ,-----------
##    | Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
##    | 
##    | Note:
##    | Input contains only lowercase English letters.
##    | Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
##    | Input length is less than 50,000.
##    | Example 1:
##    | Input: "owoztneoer"
##    | 
##    | Output: "012"
##    | Example 2:
##    | Input: "fviefuro"
##    | 
##    | Output: "45"
##    `-----------
##
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
