#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/set-mismatch/description/
## Basic Idea:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:12>
##-------------------------------------------------------------------
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        supposed_sum = (1+n)*n/2
        current_sum = 0
        for num in nums:
            current_sum += num
        l = [0] * n
        duplicate_num = -1
        for num in nums:
            if l[num-1] == 0:
                l[num-1] = 1
            else:
                duplicate_num = num
                break
        if duplicate_num == -1:
            raise Exception("Unexpected input")
        return [duplicate_num, duplicate_num + supposed_sum - current_sum]

if __name__ == '__main__':
    s = Solution()
    print s.findErrorNums([1,2,2,4])
    #print s.findErrorNums([1])
## File: test.py ends
