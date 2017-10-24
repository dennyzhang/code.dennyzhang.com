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
## Updated: Time-stamp: <2017-10-23 22:28:08>
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
