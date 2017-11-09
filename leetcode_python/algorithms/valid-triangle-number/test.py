#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #amusing, #redo, #brain
## Description:
##     https://leetcode.com/problems/valid-triangle-number/description/
##    ,-----------
##    | Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
##    | 
##    | Example 1:
##    | Input: [2,2,3,4]
##    | Output: 3
##    | Explanation:
##    | Valid combinations are: 
##    | 2,3,4 (using the first 2)
##    | 2,3,4 (using the second 2)
##    | 2,2,3
##    | Note:
##    | The length of the given array won't exceed 1000.
##    | The integers in the given array are in the range of [0, 1000].
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:14>
##-------------------------------------------------------------------
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Idea: Like 3sum
        ##       Sort the list, then use 3 loop
        ##       When the sum 2 shorter sides is greater 
        ##       than the big side, the 3 numbers can form a triangle.
        ##       Note: not O(n*n*n); numbers has 0; allow duplicate
        ##
        ## Complexity: Time O(n^2), Space O(1)
        ## Sample Data:
        ##     3, 5, 6, 7, 7, 8
        ##     i  j        k
        ##     2  2  3  4
        ##     0  0  1  1
        nums.sort()
        res = 0
        for i in range(0, len(nums)-2):
            if nums[i] == 0:
                continue
            count = 0
            k = i + 2
            for j in range(i+1, len(nums)-1):
                # k never need to move back

                # calculate current round of matches based on last round
                if (j>i+1) and (nums[i]+nums[j]>nums[k-1]):
                    count -= 1

                while k<len(nums) and nums[i]+nums[j]>nums[k]:
                    count += 1
                    k += 1
                # print("i: %d, j: %d, count: %d" % (i, j, count))
                res += count
        return res
