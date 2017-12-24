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
##     https://leetcode.com/problems/reverse-vowels-of-a-string/description/
##    ,-----------
##    | Write a function that takes a string as input and reverse only the vowels of a string.
##    | 
##    | Example 1:
##    | Given s = "hello", return "holle".
##    | 
##    | Example 2:
##    | Given s = "leetcode", return "leotcede".
##    | 
##    | Note:
##    | The vowels does not include the letter "y".
##    | 
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## Basic Idea: save vowels in an separated array
        ## Complexity: Time O(n), Space O(n)
        vowel_letters = 'aeiouAEIOU'
        length = len(s)
        vowel_list = []
        for ch in s:
            if ch in vowel_letters:
                vowel_list.append(ch)

        # reverse
        vowel_list = vowel_list[::-1]

        ret = [''] * length

        k = 0
        for i in range(0, len(s)):
            if s[i] in vowel_letters:
                ret.append(vowel_list[k])
                k += 1
            else:
                ret.append(s[i])

        return ''.join(ret)

if __name__ == '__main__':
    s = Solution()
    print s.reverseVowels("hello")
    print s.reverseVowels("leetcode")
## File: test.py ends
