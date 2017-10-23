#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/degree-of-an-array/description/
## Basic Idea:
## Complexity:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:06>
##-------------------------------------------------------------------
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the degree and digits
        digit_dict = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if digit_dict.has_key(num) is False:
                digit_dict[num] = (1, [i])
            else:
                (count, l) = digit_dict[num]
                l.append(i)
                digit_dict[num] = (count+1, l)

        degree = 0
        for num in digit_dict.keys():
            (count, _l) = digit_dict[num]
            if count > degree:
                degree = count

        min_length = 65535
        degree_digits = []
        for num in digit_dict.keys():
            (count, l) = digit_dict[num]
            if count == degree:
                start_index = l[0]
                end_index = l[-1]
                length = end_index - start_index + 1
                if length < min_length:
                    min_length = length

        # print "degree: %d, degree_digits: %s" % (degree, degree_digits)
        # loop the example, only start from digits which are in the target list
                
        return min_length

if __name__ == '__main__':
    s = Solution()
    print s.findShortestSubArray([1, 2, 2, 3, 1])
    print s.findShortestSubArray([1,2,2,3,1,4,2])
## File: test.py ends
