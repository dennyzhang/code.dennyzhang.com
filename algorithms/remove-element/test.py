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
## Basic Idea:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:13>
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
