
# Leetcode: To Lower Case     :BLOG:Basic:

---

To Lower Case  

---

Similar Problems:  

-   Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/to-lower-case)  

Credits To: [leetcode.com](https://leetcode.com/problems/to-lower-case/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/to-lower-case
    // Basic Ideas
    // Complexity: Time O(n), Space O(n)
    func toLowerCase(str string) string {
        var res string
        for _, ch := range str {
    	b := byte(ch) 
    	if b >= byte('A') && b<=byte('Z') {
    	    res += string(b+byte('a')-byte('A'))
    		} else {
    			res += string(ch)
    		}
    	}
    	return res
    }

