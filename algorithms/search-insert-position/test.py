#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description :
##     https://leetcode.com/problems/search-insert-position/description/
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-20 16:17:03>
##-------------------------------------------------------------------
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        for num in nums:
            if num >= target:
                return i
            i = i + 1
        return i

if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1,3,5,6], 5) # 2
    print s.searchInsert([1,3,5,6], 2) # 1
    print s.searchInsert([1,3,5,6], 7) # 4
    print s.searchInsert([1,3,5,6], 0) # 0
## File: test.py ends
