# Leetcode: Transpose File     :BLOG:Hard:


---

Transpose File  

---

Similar Problems:  
-   Tag: [#shell](https://code.dennyzhang.com/tag/shell)

---

Given a text file file.txt, transpose its content.  

You may assume that each row has the same number of columns and each field is separated by the ' ' character.  

For example, if file.txt has the following content:  

    name age
    alice 21
    ryan 30

Output the following:  

    name alice ryan
    age 21 30

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/transpose-file)  

Credits To: [leetcode.com](https://leetcode.com/problems/transpose-file/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/transpose-file
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
    donecat words.txt | tr -s ' ' '\
    ' | sort | uniq -c | sort -r | awk '{print $2, $1}'