#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/roman-to-integer/description/
## Tags: #redo
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:03:00>
##-------------------------------------------------------------------
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ## Idea: Compare first two, then get a common prefix. Then compare it with 3rd, then the following
        ## Complexity: Time O(n*n), Space O(1)
        str_count = len(strs)
        if str_count == 0:
            return ""
        if str_count == 1:
            return strs[0]

        common_prefix = None
        common_length = None
        for i in range(0, str_count):
            string = strs[i]
            if common_prefix is None:
                common_prefix = string
                common_length = len(common_prefix)
            else:
                common_length = min(len(string), common_length)
                for j in range(0, common_length):
                    if string[j] != common_prefix[j]:
                        common_length = j
                        break
        if common_length == 0:
            return ""
        else:
            return common_prefix[0:common_length]
