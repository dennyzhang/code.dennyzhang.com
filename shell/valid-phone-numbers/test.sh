#!/usr/bin/env bash
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: hello
## Author : Denny <contact@dennyzhang.com>
## Description:
##   https://leetcode.com/problems/valid-phone-numbers/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-17>
## Updated: Time-stamp: <2017-10-23 18:20:20>
##-------------------------------------------------------------------
set -e

grep -iE '^\([0-9][0-9][0-9]\) [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$' file.txt
## File: hello ends
