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
##     https://leetcode.com/problems/binary-watch/description/
##    ,-----------
##    | A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
##    | 
##    | Each LED represents a zero or one, with the least significant bit on the right.
##    | 
##    | 
##    | For example, the above binary watch reads "3:25".
##    | 
##    | Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
##    | 
##    | Example:
##    | 
##    | Input: n = 1
##    | Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
##    | Note:
##    | The order of output does not matter.
##    | The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
##    | The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
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
