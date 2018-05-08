# Leetcode: Unique Letter String     :BLOG:Hard:


---

Unique Letter String  

---

Similar Problems:  
-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#string](https://code.dennyzhang.com/tag/string), [#limitedrange](https://code.dennyzhang.com/tag/limitedrange)

---

A character is unique in string S if it occurs exactly once in it.  

For example, in string S = "LETTER", the only unique characters are "L" and "R".  

Let's define UNIQ(S) as the number of unique characters in string S.  

For example, UNIQ("LETTER") =  2.  

Given a string S, calculate the sum of UNIQ(substring) over all non-empty substrings of S.  

If there are two or more equal substrings at different positions in S, we consider them different.  

Since the answer can be very large, retrun the answer modulo 10 ^ 9 + 7.  

Example 1:  

    Input: "ABC"
    Output: 10
    Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
    Evey substring is composed with only unique letters.
    Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:  

    Input: "ABA"
    Output: 8
    Explanation: The same as example 1, except uni("ABA") = 1.

-   Note: 0 <= S.length <= 10000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/unique-letter-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/unique-letter-string/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/unique-letter-string
    // Basic Ideas:
    //
    //  Instead of checking how many combinations and unqiue letters, think in another way
    //  For each letter, how many ways it can form a string with its neighbors.
    //  And this letter will be unique in the string.
    //  So there would be 4 cases:
    //  - X...(X)
    //  - X
    //  - (X)...X
    //  - ...(X)...
    //
    //  We use l[26][2] to store the last two previous index of current letter
    //
    // Complexity: Time O(n), Space O(1)
    import "math"
    func uniqueLetterString(S string) int {
        res, mod := 0, int(math.Pow(10, 9)) + 7
        l := make([][2]int, 26)
        for i, _ := range l{ l[i] = [2]int{-1, -1}}
    
        for i, ch := range S {
            index := int(ch-'A')
            // only check S[0:i]. We will leave S[i:] for the last round
            res = ((i-l[index][1])*(l[index][1]-l[index][0])%mod+res)%mod
    
            l[index][0] = l[index][1]
            l[index][1] = i
        }
        for i, _ := range l{
            if l[i][1] != -1 {
                res = ((len(S)-l[i][1])*(l[i][1]-l[i][0])%mod+res)%mod
            }
        }
        return res
    }