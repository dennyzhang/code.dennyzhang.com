#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/pascals-triangle-ii/description/
## Basic Idea:
## Complexity:
## Tags: #redo
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-26 19:32:21>
##-------------------------------------------------------------------
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        l = [1] * (rowIndex + 1)
        for i in range(0, rowIndex+1):
            self.getNextRow(l, i)

        return l

    def getNextRow(self, num_list, currentRowCount):
        if currentRowCount == 0:
            num_list[0] = 1
            return

        if currentRowCount == 1:
            num_list[0] = 1
            num_list[1] = 1
            return

        # print("currentRowCount: %d" % (currentRowCount))
        for i in range(currentRowCount-1, 0, -1):
            num_list[i] = num_list[i] + num_list[i-1]
        
if __name__ == '__main__':
    s = Solution()
    s.getRow(0)
    s.getRow(1)
    s.getRow(2)
    s.getRow(3)
    s.getRow(4)
    s.getRow(5)
## File: test.py ends
