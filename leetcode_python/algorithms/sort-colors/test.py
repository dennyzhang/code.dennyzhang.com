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
        ## Idea: 2 pass. Count how many each 0, 1, 2 has happened
        ## Complexity
        ## Sample Data:
        ##     0 1 2 0 1 2 0
        ##     p           r
        ##       q
        ##     2 0
        count0, count1, count2 = 0, 0, 0
        for num in nums:
            if num == 0:
                count0 += 1
            if num == 1:
                count1 += 1
            if num == 2:
                count2 += 1

        for i in xrange(len(nums)):
            if i < count0:
                nums[i] = 0
            elif i < count0 + count1:
                nums[i] = 1
            else:
                nums[i] = 2
        
    def sortColors_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## Idea: 2 pointer. 2 pass
        ## Complexity: Time O(n), Space O(1)
        length = len(nums)
        if length<=1:
            return

        # 1st pass
        for p in xrange(length):
            if nums[p] != 0:
                break
        for q in range(p+1, length):
            if nums[q] == 0:
                nums[q] = nums[p]
                nums[p] = 0
                p += 1

        # 2nd pass
        for p in xrange(length):
            if nums[p] == 2:
                break
        for q in range(p+1, length):
            if nums[q] == 1:
                nums[q] = nums[p]
                nums[p] = 1
                p += 1
