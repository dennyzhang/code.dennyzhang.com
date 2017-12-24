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
##     https://leetcode.com/contest/weekly-contest-59/problems/self-dividing-numbers/
##    ,-----------
##    | A self-dividing number is a number that is divisible by every digit it contains.
##    | 
##    | For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
##    | 
##    | Also, a self-dividing number is not allowed to contain the digit zero.
##    | 
##    | Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
##    | 
##    | Example 1:
##    | Input: 
##    | left = 1, right = 22
##    | Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
##    | Note:
##    | 
##    | The boundaries of each input argument are 1 <= left <= right <= 10000.
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            digits = str(num)
            if '0' in digits:
                continue
            else:
                has_match = True
                for digit in digits:
                    if digit == '1':
                        continue
                    elif num % int(digit) != 0:
                        has_match = False
                        break
                if has_match:
                    res.append(num)
        return res
