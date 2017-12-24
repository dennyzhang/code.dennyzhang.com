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
##     https://leetcode.com/problems/generate-parentheses/description/
##    ,-----------
##    | Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
##    | 
##    | For example, given n = 3, a solution set is:
##    | 
##    | [
##    |   "((()))",
##    |   "(()())",
##    |   "(())()",
##    |   "()(())",
##    |   "()()()"
##    | ]
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-30 15:41:52>
##-------------------------------------------------------------------
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ## Idea: Use counter to make sure it's well-formed paretheses
        ##       Use BFS to generate the result
        ##       1. For each character, we can only print (, or )
        ##       2. unbalanced_count: How many unbalanced ( so far, 
        ##             printed_count: how many ( has already been alreay printed
        ##       3. When we can print (, if printed_count < n
        ##       4. When we can print ), if unbalanced_count > 0
        ## Complexity
        ## Sample Data:
        ##       ( stack: (
        ##       )
        if n<=0:
            return []
        res = []
        bfs_queue = []
        bfs_queue.append(("(", 1, 1))
        # loop for layer
        for i in xrange(n*2-1):
            for j in xrange(len(bfs_queue)):
                # ('((()', 3, 2)
                (output_str, printed_count, unbalanced_count) = bfs_queue[0]
                del bfs_queue[0]
                if printed_count < n:
                    bfs_queue.append(("%s(" % (output_str), \
                                        printed_count+1, unbalanced_count+1))
                if unbalanced_count > 0:
                    bfs_queue.append(("%s)" % (output_str), \
                                        printed_count, unbalanced_count-1))
        for i in xrange(len(bfs_queue)):
            res.append(bfs_queue[i][0])
        return res
