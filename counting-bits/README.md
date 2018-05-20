# Leetcode: Counting Bits     :BLOG:Medium:


---

Counting Bits  

---

Similar Problems:  
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming), [Tag: #dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's in their binary representation and return them as an array.  

Example:  
For num = 5 you should return [0,1,1,2,1,2].  

Follow up:  

-   It is very easy to come up with a solution with run time O(n\*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
-   Space complexity should be O(n).
-   Can you do it like a boss? Do it without using any builtin function like \_\_builtin\_popcount in c++ or in any other language.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/counting-bits)  

Credits To: [leetcode.com](https://leetcode.com/problems/counting-bits/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/counting-bits
    ## Basic Ideas:
    ##      If k%2 == 0, f(k) = f(k/2)
    ##      If k%2 == 1, f(k) = f(k-1)
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def countBits(self, num):
            """
            :type num: int
            :rtype: List[int]
            """
            if num == 0:
                return [0]
            if num == 1:
                return [0, 1]
            res = [0]*(num+1)
            res[0] = 0
            res[1] = 1
            for i in range(2, num+1):
                if i%2 == 0:
                    res[i] = res[i/2]
                else:
                    res[i] = res[i-1]+1
            return res