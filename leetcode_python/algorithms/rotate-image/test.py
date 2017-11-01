#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #amusing, #redo
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
        ## Basic Idea: Rotate circle by circle. From outer to inner layer.
        ##             Use an array of n to save data temporarily
        ## Complexity: Time O(n*n), Space O(n)
        length = len(matrix[0])
        if length <=1:
            return
        start_i = 0
        start_j = 0
        tmp_list = [None] * (length*4-4)

        while (length > 1):
            total_count = length*4-4
            # rotate current layer
            k = 0
            # save top
            for j in range(start_j, start_j + length):
                tmp_list[k] = matrix[start_i][j]
                k = k + 1
            #print("tmp_list: %s" % tmp_list)

            # save right
            for i in range(start_i+1, start_i + length):
                tmp_list[k] = matrix[i][start_j+length-1]
                k = k + 1
            # save bottom
            for j in range(start_j+length-2, start_j-1, -1):
                tmp_list[k] = matrix[start_i+length-1][j]
                k = k + 1
            # save left
            for i in range(start_i + length-2, start_i, -1):
                tmp_list[k] = matrix[i][start_j]
                k = k + 1

            # rotate
            k = length*3-2-1

            # change top
            for j in range(start_j, start_j + length):
                matrix[start_i][j] = tmp_list[k]
                k = (k + 1) % total_count
            # change right
            for i in range(start_i+1, start_i + length):
                matrix[i][start_j+length-1] = tmp_list[k]
                k = (k + 1) % total_count
            # change bottom
            for j in range(start_j+length-2, start_j-1, -1):
                matrix[start_i+length-1][j] = tmp_list[k]
                k = (k + 1) % total_count
            # change left
            for i in range(start_i + length-2, start_i, -1):
                matrix[i][start_j] = tmp_list[k]
                k = (k + 1) % total_count

            # go to inner layer
            start_i += 1
            start_j += 1
            length -= 2

if __name__ == '__main__':
    s = Solution()

    print s.rotate([[ 5, 1, 9,11],
                     [ 2, 4, 8,10],
                     [13, 3, 6, 7],
                     [15,14,12,16]])
    print s.rotate([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
## File: test.py ends
