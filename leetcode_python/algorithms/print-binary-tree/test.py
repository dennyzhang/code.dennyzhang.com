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
##     https://leetcode.com/problems/print-binary-tree/description/
##    ,-----------
##    | Print a binary tree in an m*n 2D string array following these rules:
##    | 
##    | The row number m should be equal to the height of the given binary tree.
##    | The column number n should always be an odd number.
##    | The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
##    | Each unused space should contain an empty string "".
##    | Print the subtrees following the same rules.
##    | Example 1:
##    | Input:
##    |      1
##    |     /
##    |    2
##    | Output:
##    | [["", "1", ""],
##    |  ["2", "", ""]]
##    | Example 2:
##    | Input:
##    |      1
##    |     / \
##    |    2   3
##    |     \
##    |      4
##    | Output:
##    | [["", "", "", "1", "", "", ""],
##    |  ["", "2", "", "", "", "3", ""],
##    |  ["", "", "4", "", "", "", ""]]
##    | Example 3:
##    | Input:
##    |       1
##    |      / \
##    |     2   5
##    |    / 
##    |   3 
##    |  / 
##    | 4 
##    | Output:
##    | 
##    | [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
##    |  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
##    |  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
##    |  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
##    | Note: The height of binary tree is in the range of [1, 10].
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ## Idea: sqrt(num)
        ## Complexity:
        ## Sample Data:
        ##    1 2 7
        if num <= 1:
            return False
        import math
        sum = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                sum += i
                if i != num/i:
                    sum += num/i
        return sum == num
