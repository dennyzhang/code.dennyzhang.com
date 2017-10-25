#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/isomorphic-strings/description/
## Tags: #redo, #amusing
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 16:38:15>
##-------------------------------------------------------------------
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## Ideas: maintain two map dictionaries.
        ##     If some characters are different, insert into the dictionary. 
        ##     If we notice a conflict, it's wrong
        ## Complexity: Time O(n), Space O(n)
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
