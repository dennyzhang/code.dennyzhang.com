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

    def sortColors_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## Idea: 3 pointers
        ##     p: where we should place 0
        ##     r: where we should place 2
        ##     q: one pass
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
        
        for p in xrange(length):
            if nums[p] != 0:
                break
        for r in range(length-1, -1, -1):
            if nums[r] != 2:
                break
        q = p+1
        while p<length and q<length and r>-1 and q<r:
            if nums[q] == 2:
                nums[q] = nums[r]
                nums[r] = 2
                r -= 1
                while r>q and nums[r] == nums[r-1] and nums[r] == 2:
                    r -= 1
            elif nums[q] == 0:
                nums[q] = nums[p]
                nums[p] = 0
                p += 1
                while p<q and nums[p] == nums[p+1] and nums[p] == 0:
                    p += 1
            else:
                while q<length-1 and q<r and nums[q] == nums[q+1]:
                    q += 1                            
