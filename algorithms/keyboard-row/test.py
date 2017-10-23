#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/keyboard-row/description/
## Basic Idea:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:15>
##-------------------------------------------------------------------
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return_list = []
        character_dict = {}
        for ch in "qwertyuiop":
            character_dict[ch] = 0
        for ch in "asdfghjkl":
            character_dict[ch] = 1
        for ch in "zxcvbnm":
            character_dict[ch] = 2

        for word in words:
            lower_word = word.lower()
            is_ok = True
            index_key = -1
            for ch in lower_word:
                if character_dict.has_key(ch) is False:
                    raise Exception("Unexpected character(%s) in %s" % (ch, word))
                if index_key == -1:
                    index_key = character_dict[ch]
                else:
                    if index_key != character_dict[ch]:
                        is_ok = False
                        break
            if is_ok is True:
                return_list.append(word)
        return return_list

if __name__ == '__main__':
    s = Solution()
    print s.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print s.findWords(["Hello", "Alaska", "Dad", "Peace", "erT"])
## File: test.py ends
