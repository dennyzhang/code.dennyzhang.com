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
##     https://leetcode.com/problems/valid-parentheses/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:11>
##-------------------------------------------------------------------
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matched_dict = {
            '(': ')',
            ')': '(',
            '[': ']',
            ']': '[',
            '{': '}',
            '}': '{'
        }

        string_stack = []

        for ch in s:
            if ch not in '()[]{}':
                raise Exception("Unexpected string: %s, character: %s" % (s, ch))
            if len(string_stack) == 0:
                string_stack.append(ch)
            else:
                if string_stack[-1] == matched_dict[ch]:
                    # pop the last item
                    string_stack.pop()
                else:
                    string_stack.append(ch)
        return len(string_stack) == 0
            
if __name__ == '__main__':
    s = Solution()
    print s.isValid("([])")
    print s.isValid("()[]{}")
    print s.isValid("()")
    print s.isValid("(]")
    print s.isValid("([)]")
## File: test.py ends
