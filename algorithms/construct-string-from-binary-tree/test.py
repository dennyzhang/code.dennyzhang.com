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
##     https://leetcode.com/problems/construct-string-from-binary-tree/description/
##    ,-----------
##    | You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
##    | 
##    | The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
##    | 
##    | Example 1:
##    | Input: Binary tree: [1,2,3,4]
##    |        1
##    |      /   \
##    |     2     3
##    |    /    
##    |   4     
##    | 
##    | Output: "1(2(4))(3)"
##    | 
##    | Explanation: Originallay it needs to be "1(2(4)())(3()())", 
##    | but you need to omit all the unnecessary empty parenthesis pairs. 
##    | And it will be "1(2(4))(3)".
##    | Example 2:
##    | Input: Binary tree: [1,2,3,null,4]
##    |        1
##    |      /   \
##    |     2     3
##    |      \  
##    |       4 
##    | 
##    | Output: "1(2()(4))(3)"
##    | 
##    | Explanation: Almost the same as the first example, 
##    | except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
##    `-----------
##
##
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
