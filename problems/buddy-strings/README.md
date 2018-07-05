
# Leetcode: Buddy Strings     :BLOG:Basic:

---

Buddy Strings  

---

Similar Problems:  

-   Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.  

Example 1:  

    Input: A = "ab", B = "ba"
    Output: true

Example 2:  

    Input: A = "ab", B = "ab"
    Output: false

Example 3:  

    Input: A = "aa", B = "aa"
    Output: true

Example 4:  

    Input: A = "aaaaaaabc", B = "aaaaaaacb"
    Output: true

Example 5:  

    Input: A = "", B = "aa"
    Output: false

Note:  

1.  0 <= A.length <= 20000
2.  0 <= B.length <= 20000
3.  A and B consist only of lowercase letters.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/buddy-strings)  

Credits To: [leetcode.com](https://leetcode.com/problems/buddy-strings/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/buddy-strings
    // Basic Ideas
    // Complexity: Time O(n+m), Space O(1)
    func buddyStrings(A string, B string) bool {
        if len(A) != len(B) { return false }
        m := map[rune]int{}
        diffList := []int{}
        for i, ch:= range A {
    	if ch != rune(B[i]) {
    	    diffList = append(diffList, i)
    	    if len(diffList) >2 { return false }
    	}
    	m[ch]++
        }
    
        if len(diffList) == 1 { return false }
        if len(diffList) == 2 { 
    	i, j:= diffList[0], diffList[1]
    	return A[i] == B[j] && A[j] == B[i]
        }
        for key := range m {
    	if m[key]>=2 { return true }
        }
        return false
    }

