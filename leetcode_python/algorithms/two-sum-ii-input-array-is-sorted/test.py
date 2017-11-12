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
##     https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
##    ,-----------
##    | Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
##    | 
##    | The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
##    | 
##    | You may assume that each input would have exactly one solution and you may not use the same element twice.
##    | 
##    | Input: numbers={2, 7, 11, 15}, target=9
##    | Output: index1=1, index2=2
##    | 
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## Basic Idea: two pointers. 1. From left to right. 2. From right to left
        ## Complexity: Time O(n), Space O(1)
        index1 = 0
        index2 = len(numbers) -1
        has_matched = False
        while index1 < index2:
            sum_value = numbers[index1] + numbers[index2]
            if sum_value == target:
                has_matched = True
                break
            elif sum_value > target:
                index2 -= 1
            else:
                index1 += 1

        if has_matched is True:
            return [index1+1, index2+1]
        else:
            return [None, None]        
## File: test.py ends
