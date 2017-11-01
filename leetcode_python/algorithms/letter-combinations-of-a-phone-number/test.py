#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #redo
## Description:
##      https://leetcode.com/problems/letter-combinations-of-a-phone-number/
##    ,-----------
##    | Given a digit string, return all possible letter combinations that the number could represent.
##    | 
##    | A mapping of digit to letters (just like on the telephone buttons) is given below.
##    | 
##    | 
##    | 
##    | Input:Digit string "23"
##    | Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
##    | Note:
##    | Although the above answer is in lexicographical order, your answer could be in any order you want.
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ## Basic Idea: recursive way
        ## Complexity:
        digit_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', \
                      '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        length = len(digits)
        if length == 0:
            return []
        elif length == 1:
            digit = digits[0]
            if digit_dict.has_key(digit) is False:
                raise Exception("Unexpected input: %s" % (digit))
            return list(digit_dict[digit])
        else:
            digit = digits[0]
            l = self.letterCombinations(digits[1:])
            ret = []
            for ch in list(digit_dict[digit]):
                for string in l:
                    ret.append(ch+string)
            return ret
            
if __name__ == '__main__':
    s = Solution()
    print s.letterCombinations("23")
## File: test.py ends
