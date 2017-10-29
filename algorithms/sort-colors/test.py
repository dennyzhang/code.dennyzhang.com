#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #amusing, #redo
## Description:
##     https://leetcode.com/problems/sort-colors/description/
##    ,-----------
##    | Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
##    | 
##    | Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
##    | 
##    | Note:
##    | You are not suppose to use the library's sort function for this problem.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 22:27:46>
##-------------------------------------------------------------------
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## Idea: 3 pointers
        ## Complexity
        ## Sample Data:
        ##     0 1 2 0 1 2 0
        ##     p           r
        ##       q
        ##     2 0
        length = len(nums)
        if length<=1:
            return
        p = 0
        r = length-1
        
        while p < length and nums[p] == 0:
            p += 1
        while r>-1 and nums[r] == 2:
            r -= 1
        
        if (p == length) or (r == 0) or (p>=r):
            return

        q = p
        while q<r and p < length and r > -1:
            if nums[q] == 1:
                q += 1
            elif nums[q] == 0:
                val = nums[q]
                nums[q] = nums[p]
                nums[p] = val
                p += 1
            else:
                val = nums[q]
                nums[q] = nums[r]
                nums[r] = val
                r -= 1
