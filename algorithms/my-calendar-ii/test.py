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
##     https://leetcode.com/contest/weekly-contest-59/problems/my-calendar-ii/
##    ,-----------
##    | Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.
##    | 
##    | Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
##    | 
##    | A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)
##    | 
##    | For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
##    | 
##    | Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
##    | Example 1:
##    | MyCalendar();
##    | MyCalendar.book(10, 20); // returns true
##    | MyCalendar.book(50, 60); // returns true
##    | MyCalendar.book(10, 40); // returns true
##    | MyCalendar.book(5, 15); // returns false
##    | MyCalendar.book(5, 10); // returns true
##    | MyCalendar.book(25, 55); // returns true
##    | Explanation: 
##    | The first two events can be booked.  The third event can be double booked.
##    | The fourth event (5, 15) can't be booked, because it would result in a triple booking.
##    | The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
##    | The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
##    | the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
##    | Note:
##    | 
##    | The number of calls to MyCalendar.book per test case will be at most 1000.
##    | In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ## Idea: Use xor: xor all elements in both s and t.
        ##       We will get the character.
        ##       Here we assume the input are valid
        ## Complexity: Time: O(n), Space O(1)
        ret = 0
        for ch in s:
            ret = ret ^ ord(ch)
        for ch in t:
            ret = ret ^ ord(ch)
        return chr(ret)

    def findTheDifference1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ## Idea: 2 dicts to count the occurences of each letter
        ## Complexity: Time: O(n), Space O(n)
        small_letters = map(chr, range(ord('a'), ord('z')+1))
        s_dict = {}
        t_dict = {}
        for ch in small_letters:
            s_dict[ch] = 0
            t_dict[ch] = 0

        for ch in s:
            s_dict[ch] += 1

        for ch in t:
            t_dict[ch] += 1

        # Check status
        ch_ret = None
        has_found = False
        for ch in small_letters:
            if s_dict[ch] == t_dict[ch]:
                continue
            elif s_dict[ch] != t_dict[ch] -1:
                return None
            else:
                if has_found is True:
                    return None
                ch_ret = ch
                has_found = True

        return ch_ret
