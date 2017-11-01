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
##     https://leetcode.com/problems/detect-capital/description/
##    ,-----------
##    | Given a word, you need to judge whether the usage of capitals in it is right or not.
##    | 
##    | We define the usage of capitals in a word to be right when one of the following cases holds:
##    | 
##    | All letters in this word are capitals, like "USA".
##    | All letters in this word are not capitals, like "leetcode".
##    | Only the first letter in this word is capital if it has more than one letter, like "Google".
##    | Otherwise, we define that this word doesn't use capitals in a right way.
##    | Example 1:
##    | Input: "USA"
##    | Output: True
##    | Example 2:
##    | Input: "FlaG"
##    | Output: False
##    | Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
##    `-----------
##
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ## Basic Idea: Scan once
        ## Complexity: Time O(n), Space O(1)
        upper_letters = map(chr, range(ord('A'), ord('Z')+1))

        length = len(word)
        upper_count = 0

        if length == 0:
            return False

        for ch in word:
            if ch in upper_letters:
                upper_count += 1

        if length == 1:
            return True
        else:
            if word[0] in upper_letters:
                return (upper_count == 1) or (upper_count == length)
            else:
                return upper_count == 0

if __name__ == '__main__':
    s = Solution()
    # print s.romanToInt("MCMXCVI")
## File: test.py ends
