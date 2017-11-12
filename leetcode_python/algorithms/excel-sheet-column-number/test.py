#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/excel-sheet-column-number/description/
##    ,-----------
##    | Given a column title as appear in an Excel sheet, return its corresponding column number.
##    | 
##    | For example:
##    | 
##    |     A -> 1
##    |     B -> 2
##    |     C -> 3
##    |     ...
##    |     Z -> 26
##    |     AA -> 27
##    |     AB -> 28 
##    `-----------
##
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Basic Idea: Convert 26 bits
        ## Complexity: Time O(n), Space, O(1)
        letter_dict = {}
        i = 1
        for ch in map(chr, range(ord('A'), ord('Z')+1)):
            letter_dict[ch] = i
            i = i + 1

        value = 0
        # print letter_dict
        for i in range(0, len(s)):
            ch = s[i]
            value = value * 26 + letter_dict[ch]
        return value

if __name__ == '__main__':
    s = Solution()
    print s.titleToNumber("AA")
    print s.titleToNumber("AB")
    print s.titleToNumber("B")
## File: test.py ends
