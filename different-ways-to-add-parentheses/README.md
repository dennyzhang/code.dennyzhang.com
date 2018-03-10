# Leetcode: Different Ways to Add Parentheses     :BLOG:Hard:


---

Different Ways to Add Parentheses  

---

Similar Problems:  
-   [Tag: #divideconquer](https://brain.dennyzhang.com/tag/divideconquer)

---

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and \*.  

Example 1  

    Input: "2-1-1".
    
    ((2-1)-1) = 0
    (2-(1-1)) = 2
    Output: [0, 2]

Example 2  

    Input: "2*3-4*5"
    
    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10
    Output: [-34, -14, -10, -10, 10]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/different-ways-to-add-parentheses)  

Credits To: [leetcode.com](https://leetcode.com/problems/different-ways-to-add-parentheses/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/different-ways-to-add-parentheses
    class Solution:
        def diffWaysToCompute(self, input):
            res = 
            for i, ch in enumerate(input):
                if ch in "+-*":
                    l1 = self.diffWaysToCompute(input[:i])
                    l2 = self.diffWaysToCompute(input[i+1:])
                    for num1 in l1:
                        for num2 in l2:
                            if ch == '+': res.append(num1+num2)
                            if ch == '-': res.append(num1-num2)
                            if ch == '*': res.append(num1*num2)
            return res if res != else [int(input)]