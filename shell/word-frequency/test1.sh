#!/usr/bin/env bash
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: hello
## Author : Denny <contact@dennyzhang.com>
## Description :
##   https://leetcode.com/problems/word-frequency/description/
## --
## Created : <2017-10-17>
## Updated: Time-stamp: <2017-10-17 22:46:34>
##-------------------------------------------------------------------
set -e

output=$(cat words.txt)
words=$(echo "$output" | sed -e "s/ /\n/g")

uniq_words=$(echo "$words" | sort | uniq)
output=""

for uniq_word in $uniq_words; do
    # echo "$uniq_word"
    count=$(echo "$words" | grep "^${uniq_word}"'$' | wc -l)
    output="${output}\n${uniq_word} ${count}"
done

echo -e "$output" | grep -v '^$' | sort -n -k 2 -r
## File: hello ends
