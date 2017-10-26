#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/contains-duplicate-ii/description/
## ,-----------
## | Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
## | 
## `-----------
##
## Tags: #amusing
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 21:35:58>
##-------------------------------------------------------------------
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ## Ideas: 2 indices: i, j. j starts from i+k
        ## Complexity: 
        ##  1 5 3 4 2  k=2
        length = len(nums)        
        for i in range(0, length-k):
            for j in range(i+k, length):
                if nums[i] == nums[j]:
                    return True
        return False
