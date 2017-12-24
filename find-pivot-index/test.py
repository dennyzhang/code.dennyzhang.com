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
##     https://leetcode.com/contest/weekly-contest-58/problems/find-pivot-index/
##    ,-----------
##    | Given an array of integers nums, write a method that returns the "pivot" index of this array.
##    | 
##    | We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
##    | 
##    | If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
##    | 
##    | Example 1:
##    | Input: 
##    | nums = [1, 7, 3, 6, 5, 6]
##    | Output: 3
##    | Explanation: 
##    | The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
##    | Also, 3 is the first index where this occurs.
##    | Example 2:
##    | Input: 
##    | nums = [1, 2, 3]
##    | Output: -1
##    | Explanation: 
##    | There is no index that satisfies the conditions in the problem statement.
##    | Note:
##    | 
##    | The length of nums will be in the range [0, 10000].
##    | Each element nums[i] will be an integer in the range [-1000, 1000].
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 0:
            return -1
        if length == 1:
            return 0
        sum_nums = [0]*length
        sum_nums[0] = nums[0]
        for i in range(1, length):
            sum_nums[i] = sum_nums[i-1] + nums[i]
        total_sum = sum_nums[-1]

        # corner case: pivot at the left
        if sum_nums[-1] - nums[0] == 0:
            return 0

        for i in xrange(1, length-1):
            if float(total_sum - nums[i])/2 == sum_nums[i-1]:
                return i

        # corner case: pivot at the right
        if sum_nums[-2] == 0:
            return length-1            
        return -1