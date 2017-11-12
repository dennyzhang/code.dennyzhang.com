#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/subsets/description/
##    ,-----------
##    | Given a set of distinct integers, nums, return all possible subsets (the power set).
##    | 
##    | Note: The solution set must not contain duplicate subsets.
##    | 
##    | For example,
##    | If nums = [1,2,3], a solution is:
##    | 
##    | [
##    |   [3],
##    |   [1],
##    |   [2],
##    |   [1,2,3],
##    |   [1,3],
##    |   [2,3],
##    |   [1,2],
##    |   []
##    | ]
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## Idea: Bit manipulation. The combination is 2**num. 
        ##       1. Generate a seed from 0 to 2**num-1
        ##       2. Then check all binary bits of that value. 
        ##       3. If any digit it's 1, show the corresponding value
        ## Complexity: 
        ##  1 2 3
        ##  0 0 0
        ##  0 0 1
        ##  0 1 0
        ##  ...
        ret = []
        length = len(nums)
        for i in range(0, 2**length):
            item = []
            for j in range(0, length):
                if i % 2 == 1:
                    item.append(nums[length-1-j])
                i = i/2
            ret.append(item)
        return ret