#!/usr/bin/env bash
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: hello
## Author : Denny <contact@dennyzhang.com>
## Description :
##   https://leetcode.com/problems/tenth-line/description/
## --
## Created : <2017-10-17>
## Updated: Time-stamp: <2017-10-17 21:37:39>
##-------------------------------------------------------------------
set -e

line_count=$(wc -l ./file.txt | awk -F' ' '{print $1}')
if [ $line_count -lt 10 ]; then
    echo ""
    exit 1
else
    head -n10 ./file.txt | tail -n1
fi
## File: hello ends
