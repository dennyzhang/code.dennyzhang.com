#!/usr/bin/env bash
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: hello
## Author : Denny <http://brain.dennyzhang.com/contact>
## Description:
##   https://leetcode.com/problems/word-frequency/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-17>
## Updated: Time-stamp: <2018-01-30 19:22:47>
##-------------------------------------------------------------------
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\
' | sort | uniq -c | sort -r | awk '{print $2, $1}'