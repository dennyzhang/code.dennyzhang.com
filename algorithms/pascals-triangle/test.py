#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/pascals-triangle/description/
## Basic Idea:
## Tags:
##     [i][j] = [i-1][j-1]+[i-1][j]
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:14>
##-------------------------------------------------------------------
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        if numRows == 1:
            l.append([1])

        if numRows >= 2:
            l.append([1])
            l.append([1, 1])

        j = 3
        for i in range(2, numRows):
            item = []
            item.append(1)
            for k in range(1, j-1):
                item.append(l[i-1][k-1] + l[i-1][k])
            item.append(1)
            l.append(item)
            j += 1 

        return l

if __name__ == '__main__':
    s = Solution()
    print s.generate(1)
    print s.generate(2)
    print s.generate(5)
    print s.generate(4)
## File: test.py ends
