# Leetcode: ZigZag Conversion     :BLOG:Medium:


---

ZigZag Conversion  

---

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)  

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"  
Write the code that will take a string and make this conversion given a number of rows:  

    string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".  

Background: what is ZigZag. [leetcode.com](https://leetcode.com/problems/zigzag-conversion/description/)  

    /*n=numRows
    2n-2    1                           2n-1                         4n-3
            2                     2n-2  2n                    4n-4   4n-2
            3               2n-3        2n+1              4n-5       .
            .           .               .               .            .
            .       n+2                 .           3n               .
            n-1 n+1                     3n-3    3n-1                 5n-5
    2n-2    n                           3n-2                         5n-4
    */
    Be careful with nR=1 && nR=2

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/zigzag-conversion)  

Credits To: [leetcode.com](https://leetcode.com/problems/zigzag-conversion/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/zigzag-conversion
    class Solution(object):
        def convert(self, s, numRows):
            """
            :type s: str
            :type numRows: int
            :rtype: str
            """