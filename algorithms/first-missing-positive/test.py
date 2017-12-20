#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #amusing, #redo, #todobrain
## Description:
##     https://leetcode.com/problems/first-missing-positive/description/
## ,-----------
## | Given an unsorted integer array, find the first missing positive integer.
## | 
## | For example,
## | Given [1,2,0] return 3,
## | and [3,4,-1,1] return 2.
## | 
## | Your algorithm should run in O(n) time and uses constant space.
## `-----------
## 
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 17:22:00>
##-------------------------------------------------------------------
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Basic Idea: count sort
        ## Complexity:
        ## Sample Data:
        ##    1  2  0
        ##    3  4  0  1
        ##    0  4  3  1
        ##    0  1  3  4
        length = len(nums)
        # set negative elements to 0s, and set elements bigger than length to 0s
        for i in xrange(length):
            if nums[i] < 0:
                nums[i] = 0
            if nums[i] > length:
                nums[i] = 0

        i = 0
        while i < length:
            j = nums[i] - 1
            if nums[i] == i+1 or nums[i] == 0 \
               or nums[i] == nums[j]:
                i = i + 1
            else:
                # swap
                nums[i], nums[j] = nums[j], nums[i]

        # get result
        for i in xrange(length):
            if nums[i] != i+1:
                return i+1
        return length+1

if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive([3,4,-1,1])
