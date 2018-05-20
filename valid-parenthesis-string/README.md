# Leetcode: Valid Parenthesis String     :BLOG:Amusing:


---

Valid Parenthesis String  

---

Similar Problems:  
-   [Swap Adjacent in LR String](https://code.dennyzhang.com/swap-adjacent-in-lr-string)
-   Tag: [#parentheses](https://code.dennyzhang.com/category/parentheses), [#string](https://code.dennyzhang.com/category/string)

---

Given a string containing only three types of characters: '(', ')' and '\*', write a function to check whether this string is valid. We define the validity of a string by these rules:  

Any left parenthesis '(' must have a corresponding right parenthesis ')'.  
Any right parenthesis ')' must have a corresponding left parenthesis '('.  
Left parenthesis '(' must go before the corresponding right parenthesis ')'.  
'\*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.  
An empty string is also valid.  

Example 1:  

    Input: "()"
    Output: True

Example 2:  

    Input: "(*)"
    Output: True

Example 3:  

    Input: "(*))"
    Output: True

Note:  
-   The string size will be in the range [1, 100].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-parenthesis-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-parenthesis-string/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/valid-parenthesis-string
    // Basic Ideas:
    //   Two pass. From left to right; From right to left
    //   l_count: (
    //   r_count: )
    //   s_count: *
    // Complexity:
    func checkValidString(s string) bool {
        l_count, r_count, s_count := 0, 0, 0
        // from left to right
        for _, ch := range s {
            if ch == '(' {
                l_count += 1
            } else {
                if ch == '*' {
                    s_count += 1
                } else {
                    if l_count+s_count == 0 { return false }
                    if l_count > 0 {
                        l_count-=1
                    } else {
                        s_count-=1
                    }
                }
            }
        }
        if s_count<l_count { return false }
        // from right to left
        l_count, r_count, s_count = 0, 0, 0
        for i:=len(s)-1; i>=0; i-- {
            ch := s[i]
            if ch == ')' {
                r_count += 1
            } else {
                if ch == '*' {
                    s_count += 1
                } else {
                    if r_count+s_count==0 { return false }
                    if r_count>0 {
                        r_count -= 1
                    } else {
                        s_count -= 1
                    }
                }
            }
        }
        if s_count<r_count { return false }
        return true
    }