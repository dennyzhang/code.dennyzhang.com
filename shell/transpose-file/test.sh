#!/usr/bin/env bash
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.sh
## Author : Denny <contact@dennyzhang.com>
## Description:
##   https://leetcode.com/problems/transpose-file/description/
## Basic Idea:
## --
## Created : <2017-10-17>
## Updated: Time-stamp: <2017-10-23 13:19:40>
##-------------------------------------------------------------------
set -e

one_line=($(head -n1 ./file.txt))
column_count=${#one_line[@]}
line_count=$(wc -l ./file.txt | awk -F' ' '{print $1}')

# echo "column_count: $column_count, line_count: $line_count"
output=($(cat ./file.txt))
# echo "output: $output"

for((i=0; i<$column_count; i++)); do
    for((j=0; j<$line_count; j++)); do
        index=$((i+j*column_count))
        if [ $((j+1)) -eq $line_count ]; then
            echo -n "${output[$index]}"
        else
            echo -n "${output[$index]} "
        fi
        # echo "${output[$index} "
    done
    echo ""
done
## File: test.sh ends
