#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/add-strings/description/
## Basic Idea:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 13:16:29>
##-------------------------------------------------------------------
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        str_num1 = num1[::-1]
        len_num1 = len(num1)

        str_num2 = num2[::-1]
        len_num2 = len(num2)
        
        has_carry = False
        i = 0
        j = 0

        ret = []
        while i < len_num1 and j < len_num2:
            digit_sum = int(str_num1[i]) + int(str_num2[j])
            if has_carry is True:
                digit_sum += 1

            if digit_sum >= 10:
                has_carry = True
            else:
                has_carry = False
            digit_sum = digit_sum % 10
            ret.append(str(digit_sum))
            i += 1
            j += 1

        while i < len_num1:
            digit_sum = int(str_num1[i])
            if has_carry is True:
                digit_sum += 1
            if digit_sum >= 10:
                has_carry = True
            else:
                has_carry = False
            digit_sum = digit_sum % 10
            ret.append(str(digit_sum))
            i += 1

        while j < len_num2:
            digit_sum = int(str_num2[j])
            if has_carry is True:
                digit_sum += 1
            if digit_sum >= 10:
                has_carry = True
            else:
                has_carry = False
            digit_sum = digit_sum % 10
            ret.append(str(digit_sum))
            j += 1

        if has_carry is True:
            ret.append("1")
        return "".join(ret[::-1])
            
if __name__ == '__main__':
    s = Solution()
    print s.addStrings("12341434141", "2341434141")
## File: test.py ends
