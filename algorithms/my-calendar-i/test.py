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
##     https://leetcode.com/contest/weekly-contest-59/problems/my-calendar-i/
##    ,-----------
##    | Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
##    | 
##    | Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
##    | 
##    | A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
##    | 
##    | For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
##    | 
##    | Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
##    | Example 1:
##    | MyCalendar();
##    | MyCalendar.book(10, 20); // returns true
##    | MyCalendar.book(15, 25); // returns false
##    | MyCalendar.book(20, 30); // returns true
##    | Explanation: 
##    | The first event can be booked.  The second can't because time 15 is already booked by another event.
##    | The third event can be booked, as the first event takes every time less than 20, but not including 20.
##    | Note:
##    | 
##    | The number of calls to MyCalendar.book per test case will be at most 1000.
##    | In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
##    `-----------
## 
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class MyCalendar(object):

    def __init__(self):
        self.start_list = []
        self.end_list = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start > end:
            return False

        length = len(self.start_list)
        if length == 0:
            self.start_list.append(start)
            self.end_list.append(end)
            return True

        i = 0
        while i < length:
            if start > self.start_list[i]:
                i += 1
            elif start == self.start_list[i]:
                return False
            else:
                break
        if i == length:
            if self.end_list[i-1] <= start:
                self.start_list.append(start)
                self.end_list.append(end)
                return True
            else:
                return False
        else:
            if i>0 and start < self.end_list[i-1]:
                return False

            if end <= self.start_list[i]:
                self.start_list.insert(i, start)
                self.end_list.insert(i, end)
                return True
            else:
                return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# obj = MyCalendar()
# print obj.book(47,50)
# print obj.book(33,41)
# print obj.book(39,45)
# print obj.book(33,42)
# print obj.book(25,32)
# print obj.book(26,35)
# print obj.book(19,25)
# print obj.book(3,8)
# print obj.book(8,13)
# print obj.book(18,27)
