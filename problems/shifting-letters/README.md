
# Leetcode: Shifting Letters     :BLOG:Medium:

---

Shifting Letters  

---

Similar Problems:  

-   Tag: [#right2left](https://code.dennyzhang.com/tag/right2left), [#string](https://code.dennyzhang.com/tag/string)

---

We have a string S of lowercase letters, and an integer array shifts.  

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').  

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.  

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.  

Return the final string after all such shifts to S are applied.  

Example 1:  

    Input: S = "abc", shifts = [3,5,9]
    Output: "rpl"
    Explanation: 
    We start with "abc".
    After shifting the first 1 letters of S by 3, we have "dbc".
    After shifting the first 2 letters of S by 5, we have "igc".
    After shifting the first 3 letters of S by 9, we have "rpl", the answer.

Note:  

1.  1 <= S.length = shifts.length <= 20000
2.  0 <= shifts[i] <= 10 ^ 9

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/shifting-letters)  

Credits To: [leetcode.com](https://leetcode.com/problems/shifting-letters/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/shifting-letters
    // Basic Ideas: One pass
    //  From right to left
    // Complexity: Time O(n), Space O(1)
    func shiftingLetters(S string, shifts []int) string {
        v := 0
        for i:=len(shifts)-1; i>=0; i-- {
    	v = (v+shifts[i])%26
    	shifts[i] = v
        }
    
        res := ""
        code := 0
        for i, ch := range S {
    	code = (int(ch-'a')+shifts[i])%26
    	res += string(code+int('a'))
        }
        return res
    }

