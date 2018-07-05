
# Leetcode: Backspace String Compare     :BLOG:Basic:

---

Backspace String Compare  

---

Similar Problems:  

-   Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.  

Example 1:  

    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

Example 2:  

    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

Example 3:  

    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

Example 4:  

    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

Note:  

1.  1 <= S.length <= 200
2.  1 <= T.length <= 200
3.  S and T only contain lowercase letters and '#' characters.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/backspace-string-compare)  

Credits To: [leetcode.com](https://leetcode.com/problems/backspace-string-compare/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: Time O(n), Space O(n)

    // Blog link: https://code.dennyzhang.com/backspace-string-compare
    // Basic Ideas:
    // Complexity: Time O(n), Space O(n)
    func getString(S string) string {
        ret := []string{}
        for _, ch := range S {
    	if ch != '#' {
    	    ret = append(ret, string(ch))
    	} else {
    	    if len(ret) != 0 { ret = ret[0:len(ret)-1] }
    	}
        }
        return strings.Join(ret, "")
    }
    
    func backspaceCompare(S string, T string) bool {
        return getString(S) == getString(T)
    }

