# Leetcode: Positions of Large Groups     :BLOG:Basic:


---

Positions of Large Groups  

---

Similar Problems:  
-   Tag: [#string](https://code.dennyzhang.com/tag/string), [#padplaceholder](https://code.dennyzhang.com/tag/padplaceholder)

---

In a string S of lowercase letters, these letters form consecutive groups of the same character.  

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".  

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.  

The final answer should be in lexicographic order.  

Example 1:  

    Input: "abbxxxxzzy"
    Output: [[3,6]]
    Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Example 2:  

    Input: "abc"
    Output: []
    Explanation: We have "a","b" and "c" but no large group.

Example 3:  

    Input: "abcdddeeeeaabbbcd"
    Output: [[3,5],[6,9],[12,14]]

Note:  1 <= S.length <= 1000  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/positions-of-large-groups)  

Credits To: [leetcode.com](https://leetcode.com/problems/positions-of-large-groups/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: Special treatment for last group

    // Blog link: https://code.dennyzhang.com/positions-of-large-groups
    // Basic Ideas: two pointers
    //   groups: [start, end]
    // Complexity: Time O(n), Space O(n)
    func largeGroupPositions(S string) [][]int {
        res := [][]int{}
        start := 0
        for end := 0; end<len(S); end++ {
            // find a new group
            if S[end] != S[start] {
                if end-start>=3 {
                    res = append(res, []int{start, end-1})
                }
                start = end
            }
            // last group
            if S[end] == S[start] && end == len(S)-1 {
                if end-start>=2 {
                    res = append(res, []int{start, end})
                }
            }
        }
        return res
    }

-   Solution: padding for last group

    // Blog link: https://code.dennyzhang.com/positions-of-large-groups
    // Basic Ideas: two pointers
    //   groups: [start, end]
    // Complexity: Time O(n), Space O(n)
    func largeGroupPositions(S string) [][]int {
        res := [][]int{}
        start := 0
        // Note: ";" won't happen in S. 
        for end, ch := range S+";" {
            if ch != rune(S[start]) {
                if end-start >=3 {
                    res = append(res, []int{start, end-1})
                }
                start = end
            }
        }
        return res
    }