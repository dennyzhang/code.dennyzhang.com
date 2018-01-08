#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo, #list
## Description:
##     https://leetcode.com/contest/weekly-contest-66/problems/employee-free-time/
##    ,-----------
##    | We are given a list avail of employees, which represents the free time for each employee.
##    | 
##    | Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
##    | 
##    | Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
##    | 
##    | Example 1:
##    | Input: avails = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
##    | Output: [[3,4]]
##    | Explanation:
##    | There are a total of three employees, and all common
##    | free time intervals would be [-inf, 1], [3, 4], [10, inf].
##    | We discard any intervals that contain inf as they aren't finite.
##    | Example 2:
##    | Input: avails = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
##    | Output: [[5,6],[7,9]]
##    | (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, avails[0][0].start = 1, avails[0][0].end = 2, and avails[0][0][0] is not defined.)
##    | 
##    | Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
##    | 
##    | Note:
##    | 
##    | avails and avails[i] are lists with lengths in range [1, 50].
##    | 0 <= avails[i].start < avails[i].end <= 10^8.
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
        ## Sample Data:
        ## barfoothefoobarman -> bar foo the foo bar man

if __name__ == '__main__':
    s = Solution()
    # print s.findSubstring("barfoothefoobarman")
## File: test.py ends
