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
##     https://leetcode.com/problems/binary-watch/description/
##    ,-----------
##    | A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
##    | 
##    | Each LED represents a zero or one, with the least significant bit on the right.
##    | 
##    | 
##    | For example, the above binary watch reads "3:25".
##    | 
##    | Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
##    | 
##    | Example:
##    | 
##    | Input: n = 1
##    | Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
##    | Note:
##    | The order of output does not matter.
##    | The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
##    | The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def readBinaryWatch(self, num):
        ## Basic Ideas:
        ##         Check all possibility
        ## Complexity: Time O(1) 12*60, Space O(1)
        ## Assumptions:
        ## Sample Data:
        res = []
        for hour in xrange(12):
            for minute in xrange(60):
                if bin(hour).count('1') + bin(minute).count('1') == num:
                    res.append("%d:%02d" % (hour, minute))
        return res

    def readBinaryWatch_v1(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ## Basic Ideas:
        ##         Get all the possible combination
        ##         Check whether it's valid
        ##         Print the value with the right format
        ## Complexity: Time O(1), Space O(1)
        ## Assumptions:
        ## Sample Data:
        l = self.getResult(num, 10)
        res = []
        for item in l:
            item_str = self.formatItem(item)
            if item_str != "":
                res.append(item_str)
        return res

    def getResult(self, num, remain_digits):
        # print("remain_digits: %d" % (remain_digits))
        if remain_digits == 0 or num > remain_digits:
            return []
        if num == 0:
            return [[0] * remain_digits]
        if num == remain_digits:
            return [[1]*remain_digits]

        res = []
        res_0 = self.getResult(num, remain_digits-1)
        res_1 = self.getResult(num-1, remain_digits-1)
        if len(res_1) != 0:
            for item in res_1:
                res.append([1] + item)
        if len(res_0) != 0:
            for item in res_0:
                res.append([0] + item)
        return res

    def formatItem(self, item):
        # If valid, return ""
        hour = item[0]*8 + item[1]*4 + item[2]*2 + item[3]*1
        if hour > 11:
            return ""
        minute = item[4]*32 + item[5]*16 + item[6]*8 + item[7]*4 + item[8]*2 + item[9]*1
        if minute > 59:
            return ""
        return "%d:%02d" % (hour, minute)
        
# s = Solution()
# print s.readBinaryWatch(1)
