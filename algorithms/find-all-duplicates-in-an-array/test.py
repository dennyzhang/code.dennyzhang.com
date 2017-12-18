#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #amusing, #todobrain, #redo
## Description:
##     https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
##    ,-----------
##    | Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
##    | 
##    | Find all the elements that appear twice in this array.
##    | 
##    | Could you do it without extra space and in O(n) runtime?
##    | 
##    | Example:
##    | Input:
##    | [4,3,2,7,8,2,3,1]
##    | 
##    | Output:
##    | [2,3]
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:14>
##-------------------------------------------------------------------
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## Basic Idea: In place change, move a[i] to i + 1
        ##             Then traverse all elements.
        ##             If some element doesn't match, it's duplicated
        ## Complexity: Time O(n), Space (1)
        ##   1 2 3 4 5 6 7 8
        ##   4 3 2 7 8 2 3 2
        ##     2 3 4     7
        i = 0
        length = len(nums)
        if length < 2:
            return []

        while i < length:
            # move to next if in position or the same
            if nums[i] - 1 == i or nums[i] == nums[nums[i] - 1]:
                i = i + 1
            else:
                j = nums[i] - 1
                # swap nums[i] and nums[j]
                nums[i], nums[j] = nums[j], nums[i]
        res = []
        for i in xrange(length):
            if nums[i]  != i+1:
                res.append(nums[i])
        return res
