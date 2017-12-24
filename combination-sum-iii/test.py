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
##     https://leetcode.com/problems/combination-sum-iii/description/
##    ,-----------
##    | Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
##    | 
##    | 
##    | Example 1:
##    | 
##    | Input: k = 3, n = 7
##    | 
##    | Output:
##    | 
##    | [[1,2,4]]
##    | 
##    | Example 2:
##    | 
##    | Input: k = 3, n = 9
##    | 
##    | Output:
##    | 
##    | [[1,2,6], [1,3,5], [2,3,4]]
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:04>
##-------------------------------------------------------------------
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ## Basic Idea:
        ## Complexity:

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum3(3, 7)
    print s.combinationSum3(3, 9)
## File: test.py ends
