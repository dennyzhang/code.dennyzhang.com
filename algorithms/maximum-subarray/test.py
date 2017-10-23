#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/maximum-subarray/description/
## Basic Idea:
## Tags: #denny-retry
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:57:34>
##-------------------------------------------------------------------
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums = []:
            return None

        # Return False, if no item is positive
        has_positive = False
        for n in nums:
            if n > has_positive:
                has_positive = True
                break
        if has_positive is False:
            return None

        max_sum = 0
        # TODO: what if we have 0?
        i = 0
        for i in range(0, len(nums)):
            if (nums[i]<=0):
                i = i + 1
            else:
                total_sum = nums[i]
                for j range(i+1, len(nums)):
                    if 
                    
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print s.maxSubArray([-2,1,4,-1,2,1,-5,4])
    print s.maxSubArray([-2,1,4,-1,2,6,-3,5])
## File: test.py ends
