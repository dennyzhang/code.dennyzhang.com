#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags:
## Description:
##     https://leetcode.com/problems/course-schedule/description/
##    ,-----------
##    | There are a total of n courses you have to take, labeled from 0 to n - 1.
##    | 
##    | Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
##    | 
##    | Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
##    | 
##    | For example:
##    | 
##    | 2, [[1,0]]
##    | There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
##    | 
##    | 2, [[1,0],[0,1]]
##    | There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
##    | 
##    | Note:
##    | The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
##    | You may assume that there are no duplicate edges in the input prerequisites.
##    `-----------
##
##
## Basic Idea:
## Complexity:
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
