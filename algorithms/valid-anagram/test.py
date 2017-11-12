# -*- encoding: utf-8 -*-
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
##     https://leetcode.com/problems/valid-anagram/description/
##    ,-----------
##    | Given two strings s and t, write a function to determine if t is an anagram of s.
##    | 
##    | For example,
##    | s = "anagram", t = "nagaram", return true.
##    | s = "rat", t = "car", return false.
##    | 
##    | Note:
##    | You may assume the string contains only lowercase alphabets.
##    | 
##    | Follow up:
##    | What if the inputs contain unicode characters? How would you adapt your solution to such case?
##    | 
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ##Idea: use a dictionary
        ##Complexity: Time O(n), Space O(1)
        count_dict = {}
        for ch in s:
            if count_dict.has_key(ch):
                count_dict[ch] +=1
            else:
                count_dict[ch] = 1

        for ch in t:
            if count_dict.has_key(ch) is False:
                return False
            else:
                count_dict[ch] -= 1

        for ch in count_dict.keys():
            if count_dict[ch] != 0:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isAnagram("ab", "ba")
    print s.isAnagram("测试A", "测A试")
