# LintCode: Digital Problem     :BLOG:Basic:


---

Digital Problem  

---

Similar Problems:  
-   [Review: Recursive Problems](https://code.dennyzhang.com/review-recursive)
-   Tag: [#recursive](https://code.dennyzhang.com/tag/recursive)

---

Give a conversion rule to convert number n:  
1.  n is an odd number: n = 3 \* n + 1
2.  n is an even number: n = n / 2
3.  After several conversions, n will become 1.

Given a number n, find the times of converting to 1.  

 Notice  
1 <= n <= 1000000  

Example  

    Given n = 2, return 1.
    
    Explanation:
    2->1

    Given n = 3, return 7.
    
    Explanation:
    3->10->5->16->8->4->2->1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/digital-problem)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/digital-problem/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/digital-problem
    class Solution:
        """
        @param n: the number n 
        @return: the times n convert to 1
        """
        def digitConvert(self, n):
            if n == 1: return 0
            if n == 2: return 1
            if n%2 == 0:
                return self.digitConvert(int(n/2))+1
            else:
                return self.digitConvert(n*3+1)+1