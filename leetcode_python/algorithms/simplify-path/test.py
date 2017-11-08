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
##     https://leetcode.com/problems/simplify-path/description/
##    ,-----------
##    | Given an absolute path for a file (Unix-style), simplify it.
##    | 
##    | For example,
##    | path = "/home/", => "/home"
##    | path = "/a/./b/../../c/", => "/c"
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ## Idea:
        ##     replace // with /
        ##     replace /./ with /
        ##     remove tailing /$
        ##     then split the string by /
        ## Complexity: 
        while path != path.replace("//", "/"):
            path = path.replace("//", "/")

        path = path.replace("/./", "/")

        if path == "/":
            return path
        if path[-1] == "/":
            path = path[:-1]
        res = []
        for element in path.split("/"):
            if element == "..":
                if len(res) != 0:
                    res.pop()
            elif element == ".":
                continue
            else:
                res.append(element)

        if res == [] or res == [""]:
            return "/"
        else:
            res = "/".join(res)
            if res[0] != "/":
                res = "/" + res
            return res
