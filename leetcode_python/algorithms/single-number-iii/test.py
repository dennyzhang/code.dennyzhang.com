#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags:
## Description:
##     https://leetcode.com/problems/single-number-iii/description/
##    ,-----------
##    | Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
##    | 
##    | For example:
##    | 
##    | Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
##    | 
##    | Note:
##    | The order of the result is not important. So in the above example, [5, 3] is also correct.
##    | Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## Idea: C = A xor B. C won't be 0. Let's say the kth digit is 1. (From right to left)
        ##       Divide the group into 2: whether kth digit is 1 or not.
        ##       A, B will be in different group. 
        ##       For each pairs of other elements, they will either be in group1 or group2
        ##       XOR of two group, we will get A and B respectively
        ##       
        ## Complexity: Time O(n), Space O(1)
        c = 0
        for num in nums:
            c = c ^ num
        k = 0
        while c%2 == 0:
            c = c/2
            k += 1

        a = 0
        b = 0
        for num in nums:
            val = num
            for i in xrange(k):
                val = val/2
            if val%2 == 0:
                a = a ^ num
            else:
                b = b ^ num
        return [a, b]
