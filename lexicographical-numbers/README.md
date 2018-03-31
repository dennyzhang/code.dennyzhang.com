# Leetcode: Lexicographical Numbers     :BLOG:Medium:


---

Given an integer n, return 1 - n in lexicographical order.  

---

Similar Problems:  
-   [Gray Code](https://brain.dennyzhang.com/gray-code)

---

Given an integer n, return 1 - n in lexicographical order.  

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].  

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/lexicographical-numbers)  

Credits To: [leetcode.com](https://leetcode.com/problems/lexicographical-numbers/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/lexicographical-numbers
    ## Basic Ideas: DFS
    ##
    ##  When to push? How to find the neighbors?
    ##
    ## Complexity: Time O(k), Space O(d)
    ##             k = size of final result
    ##             d = digits of n
    class Solution:
        def lexicalOrder(self, n):
            """
            :type n: int
            :rtype: List[int]
            """
            res, stack = [], []
            v = 1
            while v <= n:
                res.append(v)
                stack.append(v)
                v = v*10
    
            while len(stack) != 0:
                v = stack.pop()+1
                while v <= n:
                    res.append(v)
                    if v % 10 != 9:
                        stack.append(v)
                    v = v*10
            return res