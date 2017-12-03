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
##     https://leetcode.com/problems/path-sum-iii/description/
##    ,-----------
##    | You are given a binary tree in which each node contains an integer value.
##    | 
##    | Find the number of paths that sum to a given value.
##    | 
##    | The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
##    | 
##    | The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
##    | 
##    | Example:
##    | 
##    | root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
##    | 
##    |       10
##    |      /  \
##    |     5   -3
##    |    / \    \
##    |   3   2   11
##    |  / \   \
##    | 3  -2   1
##    | 
##    | Return 3. The paths that sum to 8 are:
##    | 
##    | 1.  5 -> 3
##    | 2.  5 -> 2 -> 1
##    | 3. -3 -> 11
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ## Basic Idea:
        ## Complexity: Time O(), Space O()
        ## Assumptions:
        ## barfoothefoobarman -> bar foo the foo bar man

if __name__ == '__main__':
    s = Solution()
    # print s.findSubstring("barfoothefoobarman")
## File: test.py ends
