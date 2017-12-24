#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/search-a-2d-matrix/description/
##    ,-----------
##    | Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
##    | 
##    | Integers in each row are sorted from left to right.
##    | The first integer of each row is greater than the last integer of the previous row.
##    | For example,
##    | 
##    | Consider the following matrix:
##    | 
##    | [
##    |   [1,   3,  5,  7],
##    |   [10, 11, 16, 20],
##    |   [23, 30, 34, 50]
##    | ]
##    | Given target = 3, return true.
##    | 
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ## Basic Idea: binary search
        ##             Identity which row; then check whether it exists in the specific row
        ## Complexity: Time O(log(n)), Space O(1)
        ## Assumptions:
        ## Sample Data:

        # Identity which row
        row_count = len(matrix)
        if row_count == 0:
            return False

        column_count = len(matrix[0])
        if column_count == 0:
            return False

        left, right = 0, row_count - 1
        while left <= right:
            mid = left + (right - left)/2
            if matrix[mid][0] < target:
                # right part
                left = mid + 1
            elif matrix[mid][0] > target:
                # left part
                right = mid - 1
            else:
                return True
                
        # 2    5    7
        #         6 
        # binary search will evetually narrow down to one single element
        #
        #  right mid(left)
        #        mid(right) left
        #
        # print("left:%d, right: %d" % (left, right))
        # search the specific row
        row_index = min(left, right)
        if row_index == -1:
            return False
        left, right = 0, column_count - 1
        while left <= right:
            mid = left + (right - left)/2
            if matrix[row_index][mid] < target:
                # right part
                left = mid + 1
            elif matrix[row_index][mid] > target:
                # left part
                right = mid - 1
            else:
                return True
        return False
