#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
## ,-----------
## | Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
## | 
## | Find all the elements of [1, n] inclusive that do not appear in this array.
## | 
## | Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
## | 
## | Example:
## | 
## | Input:
## | [4,3,2,7,8,2,3,1]
## | 
## | Output:
## | [5,6]
## `-----------
##
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 23:24:46>
##-------------------------------------------------------------------
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Basic Idea: traverse each item, check whether s[i] == i+1. If not, update s[s[i]-1]
        ## Complexity:
        ##  1,2,3,4,5,6,7,8
        ##
        ##  4,3,2,7,8,2,3,1
        ##  1,2,3,4,    7,8     

if __name__ == '__main__':
    s = Solution()
    # print s.romanToInt("MCMXCVI")
## File: test.py ends
