# Leetcode: Tenth Line     :BLOG:Medium:


---

Tenth Line  

---

Similar Problems:  
-   Tag: [#shell](https://brain.dennyzhang.com/tag/shell)

---

How would you print just the 10th line of a file?  

For example, assume that file.txt has the following content:  

    Line 1
    Line 2
    Line 3
    Line 4
    Line 5
    Line 6
    Line 7
    Line 8
    Line 9
    Line 10

Your script should output the tenth line, which is:  

    Line 10

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/tenth-line)  

Credits To: [leetcode.com](https://leetcode.com/problems/tenth-line/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/tenth-line
    line_count=$(wc -l ./file.txt | awk -F' ' '{print $1}')
    if [ $line_count -lt 10 ]; then
        echo ""
        exit 1
    else
        head -n10 ./file.txt | tail -n1
    fi