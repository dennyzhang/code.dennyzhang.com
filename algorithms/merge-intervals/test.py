#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/merge-intervals/description/
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 21:12:55>
##-------------------------------------------------------------------
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ## Basic Idea: Sort by first elements, then merge
        ## Complexity: Time O(nlog(n)), Space O(1)
        intervals = sorted(intervals, key=lambda x: x[0])

        ret = []

        index = 0
        for entry in intervals:
            [start_val, end_val] = entry
            if index == 0:
                ret.append(entry)
                index += 1
            else:
                [result_start_val, result_end_val] = ret[index-1]
                if start_val == result_start_val or start_val <= result_end_val:
                    ret[index-1][1] = max(end_val, result_end_val)
                else:
                    ret.append(entry)
                    index += 1
        return ret
                    
if __name__ == '__main__':
    s = Solution()
    print s.merge([[1,3],[8,10],[2,6],[15,18]])
## File: test.py ends
