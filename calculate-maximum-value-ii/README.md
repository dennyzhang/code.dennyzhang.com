# LintCode: Calculate Maximum Value II     :BLOG:Hard:


---

Calculate Maximum Value II  

---

Given a string of numbers, write a function to find the maximum value from the string, you can add a + or \* sign between any two numbers，It's different with Calculate Maximum Value, You can insert parentheses anywhere.  

Example  

    Given str = 01231, return 12
    (0 + 1 + 2) * (3 + 1) = 12 we get the maximum value 12

    Given str = 891, return 80
    As 8 * (9 + 1) = 80, so 80 is maximum.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/calculate-maximum-value-ii)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/calculate-maximum-value-ii/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/calculate-maximum-value-ii
    class Solution:
        """
        @param str: a string of numbers
        @return: the maximum value
        """
        def maxValue(self, str):
            # write your code here