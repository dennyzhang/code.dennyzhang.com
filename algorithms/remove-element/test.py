#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/remove-element/description/
##    ,-----------
##    | Given an array and a value, remove all instances of that value in place and return the new length.
##    | 
##    | Do not allocate extra space for another array, you must do this in place with constant memory.
##    | 
##    | The order of elements can be changed. It doesn't matter what you leave beyond the new length.
##    | 
##    | Example:
##    | Given input array nums = [3,2,2,3], val = 3
##    | 
##    | Your function should return length = 2, with the first two elements of nums being 2.
##    `-----------
##
## Basic Idea:
## Complexity:
## Tags: #redo
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:04>
##-------------------------------------------------------------------
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1
        return j

if __name__ == '__main__':
    s = Solution()
    print s.removeElement([3,2,2,3], 3)
    print s.removeElement([3], 3)
    print s.removeElement([], 3)
    print s.removeElement([3], 2)
## File: test.py ends
