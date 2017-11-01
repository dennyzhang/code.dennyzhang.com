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
##     https://leetcode.com/problems/3sum/description/
##    ,-----------
##    | Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
##    | 
##    | Note: The solution set must not contain duplicate triplets.
##    | 
##    | For example, given array S = [-1, 0, 1, 2, -1, -4],
##    | 
##    | A solution set is:
##    | [
##    |   [-1, 0, 1],
##    |   [-1, -1, 2]
##    | ]
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-30 15:41:52>
##-------------------------------------------------------------------
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## Idea: sort the list, then loop with idea of 2 sum
        ##       What if you have duplicate entries?
        ##       [0, 0, 0, 0]
        ## Complexity: Time O(n*n), Space O(1)
        ## Sample Data:
        ##      -4 -1 -1 0 1 2
        ##       i l         r
        ret = []
        nums.sort()

        for i in xrange(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                val = nums[i] + nums[l] + nums[r]
                if val >0:
                    r -= 1
                elif val < 0:
                    l += 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -=1
        return ret
            
    def threeSum_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## Idea: sort the list, then loop with idea of 2 sum
        ##       What if you have duplicate entries?
        ##       [0, 0, 0, 0]
        ## Complexity: Time O(n*n), Space O(1)
        ## Sample Data:
        ##      -4 -1 -1 0 1 2
        ##       i j         k
        ret = []
        nums.sort()
        length = len(nums)
        if length < 3:
            return []

        i = 0
        while True:
            while i>0 and i<length-2 and nums[i] == nums[i-1]:
                i += 1
            if i >= length-2:
                break

            j = i+1
            k = length-1
            while j<k:
                val = nums[i] + nums[j] + nums[k]
                if val == 0:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j] == nums[j+1]:
                        j += 1
                    while j<k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                elif val > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return ret
