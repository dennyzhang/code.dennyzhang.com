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
##     https://leetcode.com/problems/word-pattern/description/
## ,-----------
## | Given a pattern and a string str, find if str follows the same pattern.
## | 
## | Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
## | 
## | Examples:
## | pattern = "abba", str = "dog cat cat dog" should return true.
## | pattern = "abba", str = "dog cat cat fish" should return false.
## | pattern = "aaaa", str = "dog cat cat dog" should return false.
## | pattern = "abba", str = "dog dog dog dog" should return false.
## | Notes:
## | You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
## `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 23:24:46>
##-------------------------------------------------------------------
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ## Idea: maintain 2 map of dictionary. If conflict, return False
        ## Algorithm: Time O(n), Space O(1)
        dict_mapping = {}
        reverse_mapping = {}
        length1 = len(pattern)
        str_list = str.split(" ")
        length2 = len(str_list)

        if length1 != length2:
            return False

        for i in range(0, length1):
            ch = pattern[i]
            item = str_list[i]
            if dict_mapping.has_key(ch) is False:
                dict_mapping[ch] = item
                if reverse_mapping.has_key(item) is True and reverse_mapping[item] != ch:
                    return False
                reverse_mapping[item] = ch
            else:
                if dict_mapping[ch] != str_list[i]:
                    return False
        return True
