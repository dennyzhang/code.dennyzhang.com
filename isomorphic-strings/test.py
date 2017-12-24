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
##     https://leetcode.com/problems/isomorphic-strings/description/
## ,-----------
## | Given two strings s and t, determine if they are isomorphic.
## | 
## | Two strings are isomorphic if the characters in s can be replaced to get t.
## | 
## | All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
## | 
## | For example,
## | Given "egg", "add", return true.
## | 
## | Given "foo", "bar", return false.
## | 
## | Given "paper", "title", return true.
## | 
## | Note:
## | You may assume both s and t have the same length.
## `-----------
## 
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 23:24:46>
##-------------------------------------------------------------------
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## Ideas: maintain a dictionary for mapping
        ##     If some characters are different, insert into the dictionary. 
        ##     If we notice a conflict, it's wrong
        ## Complexity:
        ##
        ##   ab, aa
        dict_mapping = {}
        reverse_mapping = {}
        for i in range(0, len(s)):
            ch1 = s[i]
            ch2 = t[i]
            if dict_mapping.has_key(ch1) is False:
                dict_mapping[ch1] = ch2
                if reverse_mapping.has_key(ch2) and reverse_mapping[ch2] != ch1:
                    return False
                reverse_mapping[ch2] = ch1
            else:
                if dict_mapping[ch1] != ch2:
                    return False                    
        return True
