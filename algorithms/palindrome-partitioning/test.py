#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo, #todobrain, #basic
## Description:
##     https://leetcode.com/problems/palindrome-partitioning/description/
##    ,-----------
##    | Given a string s, partition s such that every substring of the partition is a palindrome.
##    | 
##    | Return all possible palindrome partitioning of s.
##    | 
##    | For example, given s = "aab",
##    | Return
##    | 
##    | [
##    |   ["aa","b"],
##    |   ["a","a","b"]
##    | ]
##    `-----------
##
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ## Basic Idea: Divide and conquer
        ## Complexity: Time O(), Space O()
        ## Assumptions:
        ## Sample Data:
        res = []
        for i in range(0, len(s)-1):
            if self.is_palindrome(s[0:i+1]):
                l = self.partition(s[i+1:])
                # print("s: %s, s1: %s, l: %s" % (s, s[i+1:], l))
                for element in l:
                    element.insert(0, s[0:i+1])
                    res.append(element)
        if self.is_palindrome(s):
            res.append([s])

        # print("s:%s, res: %s" % (s, res))
        return res

    def is_palindrome(self, s):
        return s == s[::-1]
        