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
##     https://leetcode.com/problems/missing-number/description/
## ,-----------
## | Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
## | 
## | For example,
## | Given nums = [0, 1, 3] return 2.
## | 
## | Note:
## | Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
## `-----------
## 
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 17:06:36>
##-------------------------------------------------------------------
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Idea: Use xor
        ## Complexity: Time O(n), Space O(1)
        n = len(nums)
        xor_value = 0
        for i in range(0, n):
            xor_value = xor_value ^ (i+1) ^ nums[i]

        return xor_value

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Idea: Use xor
        ## Complexity: Time O(n), Space O(1)
        n = len(nums)
        xor_value = 0
        for i in range(0, n+1):
            xor_value = xor_value ^ i

        for i in range(0, n):
            xor_value = xor_value ^ nums[i]
        return xor_value

    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Idea: caculated the desired sum. Then add up all the numbers. Do the substraction.
        ## Complexity: Time O(n), Space O(1)
        n = len(nums)
        supposed_sum = (n * (n+1))/2
        for i in range(0, n):
            supposed_sum -= nums[i]
        return supposed_sum
