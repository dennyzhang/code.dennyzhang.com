# Leetcode: Jewels and Stones     :BLOG:Basic:


---

Jewels and Stones  

---

Similar Problems:  
-   Tag: [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.  

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".  

Example 1:  

    Input: J = "aA", S = "aAAbbbb"
    Output: 3

Example 2:  

    Input: J = "z", S = "ZZ"
    Output: 0

Note:  

-   S and J will consist of letters and have length at most 50.
-   The characters in J are distinct.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/jewels-and-stones)  

Credits To: [leetcode.com](https://leetcode.com/problems/jewels-and-stones/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/jewels-and-stones
    // Basic Ideas: set/hashmap
    // Complexity: Time O(n), Space O(n)
    func numJewelsInStones(J string, S string) int {
        m := make(map[rune]bool)
        for _, ch := range J { m[ch] = true }
    
        res := 0
        for _, ch := range S {
            _, status := m[ch]
            if status == true { res += 1 }
        }
        return res
    }