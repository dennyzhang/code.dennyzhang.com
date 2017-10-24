#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/rotate-image/description/
##    ,-----------
##    | You are given an n x n 2D matrix representing an image.
##    | 
##    | Rotate the image by 90 degrees (clockwise).
##    | 
##    | Note:
##    | You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
##    | 
##    | Example 1:
##    | 
##    | Given input matrix = 
##    | [
##    |   [1,2,3],
##    |   [4,5,6],
##    |   [7,8,9]
##    | ],
##    | 
##    | rotate the input matrix in-place such that it becomes:
##    | [
##    |   [7,4,1],
##    |   [8,5,2],
##    |   [9,6,3]
##    | ]
##    | Example 2:
##    | 
##    | Given input matrix =
##    | [
##    |   [ 5, 1, 9,11],
##    |   [ 2, 4, 8,10],
##    |   [13, 3, 6, 7],
##    |   [15,14,12,16]
##    | ], 
##    | 
##    | rotate the input matrix in-place such that it becomes:
##    | [
##    |   [15,13, 2, 5],
##    |   [14, 3, 4, 1],
##    |   [12, 6, 8, 9],
##    |   [16, 7,10,11]
##    | ]
##    `-----------
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 15:58:18>
##-------------------------------------------------------------------
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ## Basic Idea:
        ## Complexity:
        i = 0
        j = 0

if __name__ == '__main__':
    s = Solution()
    print s.rotate([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

    print s.rotate([[[ 5, 1, 9,11],
                     [ 2, 4, 8,10],
                     [13, 3, 6, 7],
                     [15,14,12,16]]])
## File: test.py ends
