# Leetcode: Hand of Straights     :BLOG:Medium:


---

Hand of Straights  

---

Similar Problems:  
-   Tag: [#array](https://code.dennyzhang.com/tag/array), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Alice has a hand of cards, given as an array of integers.  

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.  

Return true if and only if she can.  

Example 1:  

    Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
    Output: true
    Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:  

    Input: hand = [1,2,3,4,5], W = 4
    Output: false
    Explanation: Alice's hand can't be rearranged into groups of 4.

Note:  

1.  1 <= hand.length <= 10000
2.  0 <= hand[i] <= 10^9
3.  1 <= W <= hand.length

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/hand-of-straights)  

Credits To: [leetcode.com](https://leetcode.com/problems/hand-of-straights/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: XXX

**General Thinkings:**  


**Key Observations:**  


**Walk Through Testdata**  

---


    // Blog link: https://code.dennyzhang.com/hand-of-straights
    // Basic Ideas: hashmap + sort
    // The start with the mininum items
    // Complexity: Time O(n*log(n))), Space O(n)
    func isNStraightHand(hand int, W int) bool {
        m := map[int]int{}
        list := int{}
        for _, v := range hand { m[v]++ }
        for key := range m { list = append(list, key) }
        sort.Ints(list)
        for _, v := range list {
            for m[v] != 0 {
                m[v]--
                // note: this step won't be O(n*W). It will be O(n) only
                for k:=1; k<W; k++ {
                    // fmt.Println(v, k, m)
                    if m[v+k] == 0 { return false }
                    m[v+k]--
                }
            }
        }
        return true
    }