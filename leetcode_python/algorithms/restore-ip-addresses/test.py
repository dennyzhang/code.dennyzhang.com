#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #amusing
## Description:
##     https://leetcode.com/problems/restore-ip-addresses/description/
## ,-----------
## | Given a string containing only digits, restore it by returning all possible valid IP address combinations.
## | 
## | For example:
## | Given "25525511135",
## | 
## | return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
## `-----------
## 
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:05:59>
##-------------------------------------------------------------------
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ## Idea: recursive way
        ## Complexity:
        return self._restoreIpAddresses(s, 4)
        
    def _restoreIpAddresses(self, s, separate_count):
        """
        :type s: str
        :rtype: List[str]
        """
        if s == "":
            return []
        if separate_count == 1:
            if self._isValid(s):
                return [s]
            else:
                return []

        res = []

        cur_segement = s[:1]
        if self._isValid(cur_segement):
            l = self._restoreIpAddresses(s[1:], separate_count-1)
            for element in l:
                res.append("%s.%s" % (cur_segement, element))
        
        cur_segement = s[:2]
        if self._isValid(cur_segement):
            l = self._restoreIpAddresses(s[2:], separate_count-1)
            for element in l:
                res.append("%s.%s" % (cur_segement, element))

        cur_segement = s[:3]
        if self._isValid(cur_segement):
            l = self._restoreIpAddresses(s[3:], separate_count-1)
            for element in l:
                res.append("%s.%s" % (cur_segement, element))
        return res
    
    def _isValid(self, s):
        if s == "":
            return False

        if len(s) > 1 and s[0] == '0':
            return False

        if int(s) > 255:
            return False

        return True
