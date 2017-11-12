#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/valid-palindrome-ii/description/
##    ,-----------
##    | Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
##    | 
##    | Example 1:
##    | Input: "aba"
##    | Output: True
##    | Example 2:
##    | Input: "abca"
##    | Output: True
##    | Explanation: You could delete the character 'c'.
##    | Note:
##    | The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
##    `-----------
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 23:54:32>
##-------------------------------------------------------------------
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Ideas: If one characters is wrong, the difference of swap and check is 1
        #        Mark the object as deleted, then examine again
        # Complexity: Time O(n), Space O(1)
        difference_index_list = []
        length = len(s)

        for i in range(0, length/2):
            if s[i] != s[length-1-i]:
                difference_index_list.append(i)

        # print("difference_index_list: %s" % (difference_index_list))
        ret = False
        if len(difference_index_list) == 0:
            ret = True
        elif len(difference_index_list) != 1:
            ret = False
        else:
            index1 = difference_index_list[0]
            for i in range(0, length/2):
                if i == index1:
                    continue
                if s[i] != s[length-1-i]:
                    ret = False
                    break
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.validPalindrome("abca") # True
    # print s.validPalindrome("aba") # True
    # print s.validPalindrome("abc") # False
## File: test.py ends
