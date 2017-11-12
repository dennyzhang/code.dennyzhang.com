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
##     https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:05:14>
##-------------------------------------------------------------------
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        ret = 0
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                ret += 1
                nums[ret] = nums[i+1]
            i += 1
        return (ret + 1)

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,2])
    print s.removeDuplicates([1,2,1])
    print s.removeDuplicates([2])
    print s.removeDuplicates([])
## File: test.py ends
