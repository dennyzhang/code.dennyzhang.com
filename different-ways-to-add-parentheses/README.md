# Leetcode: Different Ways to Add Parentheses     :BLOG:Basic:


---

Different Ways to Add Parentheses  

---

Similar Problems:  
-   [Review: Linked List Problems](https://brain.dennyzhang.com/review-linkedlist), [Tag: #linkedlist](https://brain.dennyzhang.com/tag/linkedlist)

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