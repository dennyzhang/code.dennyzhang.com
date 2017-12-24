#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/degree-of-an-array/description/
##    ,-----------
##    | Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
##    | 
##    | Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
##    | 
##    | Example 1:
##    | Input: [1, 2, 2, 3, 1]
##    | Output: 2
##    | Explanation: 
##    | The input array has a degree of 2 because both elements 1 and 2 appear twice.
##    | Of the subarrays that have the same degree:
##    | [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
##    | The shortest length is 2. So return 2.
##    | Example 2:
##    | Input: [1,2,2,3,1,4,2]
##    | Output: 6
##    | Note:
##    | 
##    | nums.length will be between 1 and 50,000.
##    | nums[i] will be an integer between 0 and 49,999.
##    `-----------
##    
## Basic Idea:
## Complexity:
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
