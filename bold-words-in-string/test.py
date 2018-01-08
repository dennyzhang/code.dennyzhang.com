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
##     https://leetcode.com/contest/weekly-contest-66/problems/bold-words-in-string/
##
##    ,-----------
##    | Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.
##    | 
##    | The returned string should use the least number of tags possible, and of course the tags should form a valid combination.
##    | 
##    | For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.
##    | 
##    | Note:
##    | 
##    | words has length in range [0, 50].
##    | words[i] has length in range [1, 10].
##    | S has length in range [0, 500].
##    | All characters in words[i] and S are lowercase letters.
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
