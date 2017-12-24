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
##     https://leetcode.com/problems/plus-one/description/
##    ,-----------
##    | Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
##    | 
##    | You may assume the integer do not contain any leading zero, except the number 0 itself.
##    | 
##    | The digits are stored such that the most significant digit is at the head of the list.
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ## Idea: If the highest digit is 1, the value is negative
        ## Complexity: Time O(n), Space O(n)
        res = []
        has_carry = False
        if digits[-1] == 9:
            res.insert(0, 0)
            has_carry = True
        else:
            res.insert(0, digits[-1]+1)

        for i in range(len(digits)-2, -1, -1):
            if has_carry is False:
                res.insert(0, digits[i])
            else:
                if digits[i] == 9:
                    res.insert(0, 0)
                    has_carry = True
                else:
                    res.insert(0, digits[i]+1)
                    has_carry = False

        if has_carry is True:
            res.insert(0, 1)
        return res
