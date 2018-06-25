# Leetcode: Score of Parentheses     :BLOG:Medium:


---

Score of Parentheses  

---

Similar Problems:  
-   Tag: [#stack](https://code.dennyzhang.com/tag/stack)

---

Given a balanced parentheses string S, compute the score of the string based on the following rule:  

() has score 1  
AB has score A + B, where A and B are balanced parentheses strings.  
(A) has score 2 \* A, where A is a balanced parentheses string.  

Example 1:  

    Input: "()"
    Output: 1

Example 2:  

    Input: "(())"
    Output: 2

Example 3:  

    Input: "()()"
    Output: 2

Example 4:  

    Input: "(()(()))"
    Output: 6

Note:  

1.  S is a balanced parentheses string, containing only ( and ).
2.  2 <= S.length <= 50

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/score-of-parentheses)  

Credits To: [leetcode.com](https://leetcode.com/problems/score-of-parentheses/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/score-of-parentheses
    // Basic Ideas: Stack
    // Complexity: Time O(n), Space O(n)
    func scoreOfParentheses(S string) int {
        stack := []int{}
        for _, ch := range S {
            if ch == '(' {
                stack = append(stack, 0)
            } else {
                // Find 0 and pop it
                num := 0
                i := len(stack)-1
                for stack[i] != 0 {
                    num += stack[i]
                    i--
                }
                v:= 2*num
                if num == 0 { v = 1 }
                if i == 0 {
                    stack = []int{v}
                } else {
                    stack = stack[0:i]
                    stack = append(stack, v)
                }
            }
        }
        res := 0
        for _, num := range stack { res += num }
        return res
    }