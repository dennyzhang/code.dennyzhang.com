#!/usr/bin/env bash
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: hello
## Author : Denny <contact@dennyzhang.com>
## Description:
##   https://leetcode.com/problems/word-frequency/description/
## Basic Idea:
## --
## Created : <2017-10-17>
## Updated: Time-stamp: <2017-10-23 13:19:40>
##-------------------------------------------------------------------
set -e

uniq_words=$(sed -e "s/ /\n/g" words.txt | sed -e "s/\\n/\n/g" | sort | grep -v '^$' | uniq)
output=""

for uniq_word in $uniq_words; do
    #echo "$uniq_word"
    count=$(grep $uniq_word words.txt | sed -e "s/ /\n/g" | grep "^${uniq_word}"'$' | wc -l)
    output="${output}\n${uniq_word} ${count}"
done

echo -e "$output" | grep -v '^$' | sort -n -k 2 -r
## File: hello ends
