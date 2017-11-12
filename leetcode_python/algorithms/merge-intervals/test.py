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
##     https://leetcode.com/problems/merge-intervals/description/
##    ,-----------
##    | Given a collection of intervals, merge all overlapping intervals.
##    | 
##    | For example,
##    | Given [1,3],[2,6],[8,10],[15,18],
##    | return [1,6],[8,10],[15,18]
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:17>
##-------------------------------------------------------------------
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        for entry in sorted(intervals, key=lambda entry: entry.start):
            if ret and entry.start <= ret[-1].end:
                ret[-1].end = max(ret[-1].end, entry.end)
            else:
                ret.append(entry)
        return ret
