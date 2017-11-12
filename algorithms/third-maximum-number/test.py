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
##     https://leetcode.com/problems/third-maximum-number/description/
## Basic Idea: insert sort
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:59:10>
##-------------------------------------------------------------------
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 3
        max_list = [None] * count
        for num in nums:
            # Find where to insert
            insert_index = -1
            for i in range(0, count):
                max_value = max_list[i]
                if max_value is None:
                    insert_index = i
                    break
                elif num == max_value:
                    insert_index = -1
                    break
                elif num > max_value:
                    insert_index = i
                    break

            # insert the value
            if insert_index != -1:
                for i in range(count-1, insert_index, -1):
                    max_list[i] = max_list[i-1]
                max_list[insert_index] = num

        ret = None
        # get status
        if max_list[2] is not None:
            ret = max_list[2]
        else:
            ret = max_list[0]
        # print ret
        return ret
    
if __name__ == '__main__':
    s = Solution()
    s.thirdMax([1, 3])
    s.thirdMax([1, 2])
    s.thirdMax([3, 2, 1])
    s.thirdMax([2, 2, 3, 1])
## File: test.py ends
