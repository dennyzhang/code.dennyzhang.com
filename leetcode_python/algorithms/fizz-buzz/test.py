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
##     https://leetcode.com/problems/fizz-buzz/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:05:20>
##-------------------------------------------------------------------
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        i = 0
        while i<n:
            if (i+1) % 15 == 0:
                string = "FizzBuzz"
            elif (i+1) % 3 == 0:
                string = "Fizz"
            elif (i+1) % 5 == 0:
                string = "Buzz"
            else:
                string = str(i+1)
            ret.append(string)
            i += 1
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.fizzBuzz(4)
    print s.fizzBuzz(15)
## File: test.py ends
