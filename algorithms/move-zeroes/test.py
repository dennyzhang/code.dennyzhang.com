#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/move-zeroes/description/
##    ,-----------
##    | Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
##    | 
##    | For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
##    | 
##    | Note:
##    | You must do this in-place without making a copy of the array.
##    | Minimize the total number of operations.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## Idea: 2 pointers
        ## Complexity: Time O(n), Space O(1)
        ## 1, 2, 0, 3, 12
        ## i points to place whose value is 0
        ## j starts from i+1, point to the place of first non-Zero value
        length = len(nums)
        j = 0
        for i in range(0, length-1):
            if nums[i] == 0:
                for j in range(i+1, length):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        i = j
                        break
