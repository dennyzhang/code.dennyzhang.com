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
##     https://leetcode.com/problems/lru-cache/description/
##    ,-----------
##    | Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
##    | 
##    | get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
##    | put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
##    | 
##    | Follow up:
##    | Could you do both operations in O(1) time complexity?
##    | 
##    | Example:
##    | 
##    | LRUCache cache = new LRUCache( 2 /* capacity */ );
##    | 
##    | cache.put(1, 1);
##    | cache.put(2, 2);
##    | cache.get(1);       // returns 1
##    | cache.put(3, 3);    // evicts key 2
##    | cache.get(2);       // returns -1 (not found)
##    | cache.put(4, 4);    // evicts key 1
##    | cache.get(1);       // returns -1 (not found)
##    | cache.get(3);       // returns 3
##    | cache.get(4);       // returns 4
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ## Idea: sqrt(num)
        ## Complexity:
        ## Sample Data:
        ##    1 2 7
        if num <= 1:
            return False
        import math
        sum = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                sum += i
                if i != num/i:
                    sum += num/i
        return sum == num
