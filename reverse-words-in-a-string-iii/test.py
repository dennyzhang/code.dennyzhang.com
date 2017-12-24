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
##     https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:59:12>
##-------------------------------------------------------------------
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_word_list = []
        for word in s.split(" "):
            reversed_word_list.append(word[::-1])

        return " ".join(reversed_word_list)

if __name__ == '__main__':
    s = Solution()
    print s.reverseWords("Let's take LeetCode contest")
    print s.reverseWords("Let's")
## File: test.py ends
