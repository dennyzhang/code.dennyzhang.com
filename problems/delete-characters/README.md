# LintCode: Delete Characters     :BLOG:Basic:


---

Delete Characters  

---

Similar Problems:  
-   Tag: [#string](https://code.dennyzhang.com/tag/string), [#twopointer](https://code.dennyzhang.com/tag/twopointer)

---

Description  
Input two strings s and t,determine if s can get t after deleting some characters.  

1 <= |s|, |t| <= 10^5  

String contains only lowercase letters  

Example  

    Given s="abc", t="c" , return True.
    
    Explanation:
    s delete 'a' and 'b' to get t.

    Given s="a", t="c" , return False.
    
    Explanation:
    s cannot get t after deleting some characters.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/delete-characters)  

Credits To: [lintcode.com](https://www.lintcode.com/problem/delete-characters/description)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: twopointer

    // Blog link: https://code.dennyzhang.com/delete-characters
    // Basic Ideas: Two pointers
    // Complexity: Time O(n+m), Space O(1)
    /**
     * @param s: The string s
     * @param t: The string t
     * @return: Return if can get the string t
     */
    func canGetString (s string, t string) bool {
        i, j := 0, 0
        for i<len(s) && j<len(t) {
            if s[i] != t[j] {
                i++
                continue
            }
            i, j = i+1, j+1
        }
        return j==len(t)
    }